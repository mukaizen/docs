"""
Custom User model.

Why a custom user model?
  Django's default User has a fixed username field and limited profile fields.
  This model uses email as the primary identifier and adds common profile fields.
  It is MUCH harder to swap this out after the first migration — always do it now.

Fields added beyond Django defaults:
  - email (replaces username as unique identifier)
  - avatar
  - bio
  - phone
  - timezone
  - is_email_verified
  - created_at / updated_at
"""

import uuid

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone as tz
from django.utils.translation import gettext_lazy as _

from apps.core.models import TimeStampedModel
from .managers import UserManager


def user_avatar_path(instance, filename):
    """Upload avatars to  media/avatars/<uuid>/<filename>"""
    ext = filename.rsplit(".", 1)[-1]
    return f"avatars/{instance.pk}/{uuid.uuid4().hex}.{ext}"


class User(AbstractBaseUser, PermissionsMixin, TimeStampedModel):
    """
    Custom user model — email is the USERNAME_FIELD.

    All authentication should go through apps.users.backends if you add
    social auth or JWT — just add new backends to AUTHENTICATION_BACKENDS.
    """

    # ── Identity ──────────────────────────────────────────────────────────────
    id         = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email      = models.EmailField(_("email address"), unique=True, db_index=True)
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name  = models.CharField(_("last name"),  max_length=150, blank=True)

    # ── Profile ───────────────────────────────────────────────────────────────
    avatar   = models.ImageField(upload_to=user_avatar_path, blank=True, null=True)
    bio      = models.TextField(_("bio"), max_length=500, blank=True)
    phone    = models.CharField(_("phone number"), max_length=30, blank=True)
    timezone = models.CharField(_("timezone"), max_length=50, default="UTC")
    website  = models.URLField(_("website"), blank=True)

    # ── Status ────────────────────────────────────────────────────────────────
    is_staff         = models.BooleanField(_("staff status"), default=False)
    is_active        = models.BooleanField(_("active"), default=True)
    is_email_verified = models.BooleanField(_("email verified"), default=False)
    date_joined      = models.DateTimeField(_("date joined"), default=tz.now)

    objects = UserManager()

    USERNAME_FIELD  = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    class Meta:
        verbose_name        = _("user")
        verbose_name_plural = _("users")
        ordering            = ["-date_joined"]

    def __str__(self):
        return self.email

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}".strip() or self.email

    def get_short_name(self):
        return self.first_name or self.email.split("@")[0]

    @property
    def display_name(self):
        return self.get_full_name()

    @property
    def avatar_url(self):
        if self.avatar:
            return self.avatar.url
        return None  # return default avatar URL if you have one
