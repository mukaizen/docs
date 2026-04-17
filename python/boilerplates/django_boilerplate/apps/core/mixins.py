"""
Reusable view mixins.

Import in any view:
    from apps.core.mixins import StaffRequiredMixin, AjaxRequiredMixin
"""

from django.contrib.auth.mixins import AccessMixin, LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import JsonResponse


class StaffRequiredMixin(LoginRequiredMixin):
    """Restrict view to staff users only."""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if not request.user.is_staff:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class SuperuserRequiredMixin(LoginRequiredMixin):
    """Restrict view to superusers only."""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return self.handle_no_permission()
        if not request.user.is_superuser:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class OwnerRequiredMixin(LoginRequiredMixin):
    """
    Ensure the logged-in user owns the object.
    Override `get_owner` if ownership field is not `user` or `owner`.
    """
    owner_field = "user"   # the FK field on the model pointing to User

    def get_owner(self, obj):
        return getattr(obj, self.owner_field, None)

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        obj = self.get_object()
        if self.get_owner(obj) != request.user:
            raise PermissionDenied
        return response


class AjaxRequiredMixin(AccessMixin):
    """Return 400 for non-AJAX requests. Useful for HTMX / fetch-only endpoints."""
    def dispatch(self, request, *args, **kwargs):
        if not request.headers.get("X-Requested-With") == "XMLHttpRequest":
            return JsonResponse({"error": "AJAX request required."}, status=400)
        return super().dispatch(request, *args, **kwargs)


class SuccessMessageMixin:
    """
    Add a success message after a successful form submission.
    Requires django.contrib.messages in INSTALLED_APPS.
    """
    success_message = ""

    def form_valid(self, form):
        from django.contrib import messages
        if self.success_message:
            messages.success(self.request, self.success_message)
        return super().form_valid(form)


class PaginationMixin:
    """
    Standard pagination mixin for ListView.
    Override paginate_by in your view to set per-page count.
    """
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator   = context.get("paginator")
        page_obj    = context.get("page_obj")
        if paginator and page_obj:
            context["page_range"] = paginator.get_elided_page_range(
                page_obj.number, on_each_side=2, on_ends=1
            )
        return context
