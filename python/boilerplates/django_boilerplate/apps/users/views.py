import logging

from django.contrib import messages
from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordChangeView,
    PasswordResetView,
    PasswordResetConfirmView,
)
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView, DetailView, UpdateView, TemplateView

from .forms import RegisterForm, ProfileUpdateForm

User = get_user_model()
logger = logging.getLogger(__name__)


class RegisterView(CreateView):
    """Public user registration."""
    form_class    = RegisterForm
    template_name = "users/register.html"
    success_url   = reverse_lazy("users:login")

    def dispatch(self, request, *args, **kwargs):
        # Already logged in? Go to dashboard
        if request.user.is_authenticated:
            return redirect("users:dashboard")
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.instance
        logger.info("New user registered: %s", user.email)
        messages.success(self.request, _("Account created! Please log in."))
        return response


class CustomLoginView(LoginView):
    template_name = "users/login.html"
    redirect_authenticated_user = True

    def form_valid(self, form):
        logger.info("User logged in: %s", form.get_user().email)
        return super().form_valid(form)


class CustomLogoutView(LogoutView):
    next_page = "users:login"


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = "users/dashboard.html"


class ProfileView(LoginRequiredMixin, DetailView):
    """Read-only profile page — can be public or private."""
    model         = User
    template_name = "users/profile.html"
    context_object_name = "profile_user"
    slug_field    = "pk"
    slug_url_kwarg = "pk"

    def get_object(self, queryset=None):
        # Default: view own profile; pass pk to view another user's
        pk = self.kwargs.get("pk", self.request.user.pk)
        return User.objects.get(pk=pk)


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    """Edit own profile."""
    model         = User
    form_class    = ProfileUpdateForm
    template_name = "users/profile_edit.html"
    success_url   = reverse_lazy("users:profile")

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, _("Profile updated successfully."))
        logger.info("User %s updated their profile", self.request.user.email)
        return super().form_valid(form)


class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = "users/password_change.html"
    success_url   = reverse_lazy("users:profile")

    def form_valid(self, form):
        messages.success(self.request, _("Password changed successfully."))
        return super().form_valid(form)


class CustomPasswordResetView(PasswordResetView):
    template_name         = "users/password_reset.html"
    email_template_name   = "emails/password_reset_email.html"
    subject_template_name = "emails/password_reset_subject.txt"
    success_url           = reverse_lazy("users:password_reset_done")


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "users/password_reset_confirm.html"
    success_url   = reverse_lazy("users:password_reset_complete")


class AccountSettingsView(LoginRequiredMixin, TemplateView):
    """Account settings hub — links to profile edit, password change, etc."""
    template_name = "users/account_settings.html"


class AccountDeleteView(LoginRequiredMixin, TemplateView):
    """Soft-delete / deactivate the user account."""
    template_name = "users/account_delete.html"

    def post(self, request, *args, **kwargs):
        user = request.user
        user.is_active = False
        user.save(update_fields=["is_active"])
        logout(request)
        logger.info("User %s deactivated their account", user.email)
        messages.info(request, _("Your account has been deactivated."))
        return redirect("users:login")
