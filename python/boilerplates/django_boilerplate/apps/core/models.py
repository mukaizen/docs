"""
Core app base models.

Import TimeStampedModel (and others) in your own app models:

    from apps.core.models import TimeStampedModel

    class Post(TimeStampedModel):
        title = models.CharField(max_length=200)
        ...
"""

import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStampedModel(models.Model):
    """
    Abstract base model that adds created_at / updated_at to every model.
    Inherit from this instead of models.Model for automatic timestamps.
    """
    created_at = models.DateTimeField(_("created at"), auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(_("updated at"), auto_now=True)

    class Meta:
        abstract = True


class UUIDModel(models.Model):
    """
    Abstract base model with UUID primary key instead of auto-increment integer.
    Use this when you don't want to expose sequential IDs in URLs or APIs.
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class TimeStampedUUIDModel(UUIDModel, TimeStampedModel):
    """Convenience base: UUID pk + timestamps. Most commonly used combination."""
    class Meta:
        abstract = True


class SoftDeleteManager(models.Manager):
    """Default manager that excludes soft-deleted records."""
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)


class AllObjectsManager(models.Manager):
    """Manager that returns ALL records including soft-deleted."""
    def get_queryset(self):
        return super().get_queryset()


class SoftDeleteModel(models.Model):
    """
    Abstract model that soft-deletes records (sets deleted_at) instead of
    removing them from the DB. Hard delete is still available via .hard_delete().

    Usage:
        class Order(TimeStampedModel, SoftDeleteModel):
            ...

        order.delete()          # soft-delete: sets deleted_at
        order.restore()         # un-delete
        order.hard_delete()     # permanently removes from DB
        Order.objects.all()     # excludes deleted records (default manager)
        Order.all_objects.all() # includes deleted records
    """
    deleted_at = models.DateTimeField(_("deleted at"), null=True, blank=True, db_index=True)

    objects     = SoftDeleteManager()
    all_objects = AllObjectsManager()

    class Meta:
        abstract = True

    def delete(self, using=None, keep_parents=False):
        from django.utils import timezone
        self.deleted_at = timezone.now()
        self.save(update_fields=["deleted_at"])

    def restore(self):
        self.deleted_at = None
        self.save(update_fields=["deleted_at"])

    def hard_delete(self):
        super().delete()

    @property
    def is_deleted(self):
        return self.deleted_at is not None


class SingletonModel(models.Model):
    """
    Abstract model that allows only ONE instance.
    Great for site-wide settings stored in the database.

    Usage:
        class SiteSettings(SingletonModel):
            maintenance_mode = models.BooleanField(default=False)
            ...

        settings = SiteSettings.get_instance()
    """
    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass  # singletons cannot be deleted

    @classmethod
    def get_instance(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj
