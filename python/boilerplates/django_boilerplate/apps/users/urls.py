"""
Users app URL configuration.

All URLs are prefixed with /users/ (set in config/urls.py).

Pattern:
  /users/register/          → RegisterView
  /users/login/             → CustomLoginView
  /users/logout/            → CustomLogoutView
  /users/dashboard/         → DashboardView
  /users/profile/           → ProfileView (own)
  /users/profile/<pk>/      → ProfileView (other user)
  /users/profile/edit/      → ProfileUpdateView
  /users/settings/          → AccountSettingsView
  /users/settings/password/ → CustomPasswordChangeView
  /users/settings/delete/   → AccountDeleteView
  /users/password-reset/    → password reset flow
"""

from django.contrib.auth.views import (
    PasswordResetDoneView,
    PasswordResetCompleteView,
)
from django.urls import path

from . import views

app_name = "users"

urlpatterns = [
    # ── Auth ──────────────────────────────────────────────────────────────────
    path("register/",   views.RegisterView.as_view(),     name="register"),
    path("login/",      views.CustomLoginView.as_view(),  name="login"),
    path("logout/",     views.CustomLogoutView.as_view(), name="logout"),

    # ── Dashboard ─────────────────────────────────────────────────────────────
    path("dashboard/",  views.DashboardView.as_view(),    name="dashboard"),

    # ── Profile ───────────────────────────────────────────────────────────────
    path("profile/",             views.ProfileView.as_view(),       name="profile"),
    path("profile/<uuid:pk>/",   views.ProfileView.as_view(),       name="profile-detail"),
    path("profile/edit/",        views.ProfileUpdateView.as_view(), name="profile-edit"),

    # ── Account Settings ──────────────────────────────────────────────────────
    path("settings/",            views.AccountSettingsView.as_view(),      name="settings"),
    path("settings/password/",   views.CustomPasswordChangeView.as_view(), name="password-change"),
    path("settings/delete/",     views.AccountDeleteView.as_view(),        name="account-delete"),

    # ── Password Reset ────────────────────────────────────────────────────────
    path("password-reset/",
         views.CustomPasswordResetView.as_view(),
         name="password_reset"),
    path("password-reset/done/",
         PasswordResetDoneView.as_view(template_name="users/password_reset_done.html"),
         name="password_reset_done"),
    path("password-reset/<uidb64>/<token>/",
         views.CustomPasswordResetConfirmView.as_view(),
         name="password_reset_confirm"),
    path("password-reset/complete/",
         PasswordResetCompleteView.as_view(template_name="users/password_reset_complete.html"),
         name="password_reset_complete"),
]
