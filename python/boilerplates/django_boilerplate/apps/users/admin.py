from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    add_form    = CustomUserCreationForm
    form        = CustomUserChangeForm
    model       = User

    list_display  = ("email", "first_name", "last_name", "is_staff", "is_active", "is_email_verified", "date_joined")
    list_filter   = ("is_staff", "is_active", "is_email_verified")
    search_fields = ("email", "first_name", "last_name")
    ordering      = ("-date_joined",)
    readonly_fields = ("id", "date_joined", "created_at", "updated_at")

    fieldsets = (
        (None,            {"fields": ("id", "email", "password")}),
        (_("Personal"),   {"fields": ("first_name", "last_name", "avatar", "bio", "phone", "website", "timezone")}),
        (_("Permissions"),{"fields": ("is_active", "is_staff", "is_superuser", "is_email_verified", "groups", "user_permissions")}),
        (_("Dates"),      {"fields": ("date_joined", "created_at", "updated_at")}),
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields":  ("email", "first_name", "last_name", "password1", "password2", "is_staff", "is_active"),
        }),
    )
