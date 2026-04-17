#!/usr/bin/env python
"""
scripts/new_app.py — scaffold a new Django app with all boilerplate.

Usage:
    python scripts/new_app.py blog
    python scripts/new_app.py shop
    python scripts/new_app.py notifications

This creates apps/<name>/ with:
  models.py, views.py, urls.py, admin.py, apps.py, forms.py,
  services.py, tasks.py, signals.py
  api/__init__.py, api/serializers.py, api/views.py, api/urls.py
  tests/test_models.py, tests/test_views.py, tests/test_api.py
  migrations/__init__.py

Then tells you exactly what to add to settings + urls.
"""

import os
import sys
import textwrap

APP_NAME = sys.argv[1] if len(sys.argv) > 1 else None

if not APP_NAME:
    print("Usage: python scripts/new_app.py <appname>")
    sys.exit(1)

BASE = os.path.join(os.path.dirname(__file__), "..", "apps", APP_NAME)

DIRS = [
    BASE,
    os.path.join(BASE, "api"),
    os.path.join(BASE, "migrations"),
    os.path.join(BASE, "tests"),
]

FILES = {
    os.path.join(BASE, "__init__.py"): "",
    os.path.join(BASE, "migrations", "__init__.py"): "",
    os.path.join(BASE, "api", "__init__.py"): "",
    os.path.join(BASE, "tests", "__init__.py"): "",

    os.path.join(BASE, "apps.py"): textwrap.dedent(f"""\
        from django.apps import AppConfig


        class {APP_NAME.capitalize()}Config(AppConfig):
            default_auto_field = "django.db.models.BigAutoField"
            name  = "apps.{APP_NAME}"
            label = "{APP_NAME}"

            def ready(self):
                import apps.{APP_NAME}.signals  # noqa: F401
        """),

    os.path.join(BASE, "models.py"): textwrap.dedent(f"""\
        from django.db import models
        from apps.core.models import TimeStampedUUIDModel


        # class {APP_NAME.capitalize()}(TimeStampedUUIDModel):
        #     name = models.CharField(max_length=200)
        #
        #     class Meta:
        #         ordering = ["-created_at"]
        #
        #     def __str__(self):
        #         return self.name
        """),

    os.path.join(BASE, "admin.py"): textwrap.dedent(f"""\
        from django.contrib import admin
        # from .models import {APP_NAME.capitalize()}

        # @admin.register({APP_NAME.capitalize()})
        # class {APP_NAME.capitalize()}Admin(admin.ModelAdmin):
        #     list_display  = ("name", "created_at")
        #     search_fields = ("name",)
        #     ordering      = ("-created_at",)
        """),

    os.path.join(BASE, "forms.py"): textwrap.dedent(f"""\
        from django import forms
        # from .models import {APP_NAME.capitalize()}

        # class {APP_NAME.capitalize()}Form(forms.ModelForm):
        #     class Meta:
        #         model  = {APP_NAME.capitalize()}
        #         fields = ("name",)
        """),

    os.path.join(BASE, "views.py"): textwrap.dedent(f"""\
        import logging

        from django.contrib.auth.mixins import LoginRequiredMixin
        from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
        from django.urls import reverse_lazy

        logger = logging.getLogger(__name__)

        # from .models import {APP_NAME.capitalize()}
        # from .forms  import {APP_NAME.capitalize()}Form


        # class {APP_NAME.capitalize()}ListView(LoginRequiredMixin, ListView):
        #     model               = {APP_NAME.capitalize()}
        #     template_name       = "{APP_NAME}/{APP_NAME}_list.html"
        #     context_object_name = "{APP_NAME}s"
        #     paginate_by         = 20
        """),

    os.path.join(BASE, "urls.py"): textwrap.dedent(f"""\
        from django.urls import path
        from . import views

        app_name = "{APP_NAME}"

        urlpatterns = [
            # path("",          views.{APP_NAME.capitalize()}ListView.as_view(),   name="list"),
            # path("<uuid:pk>/", views.{APP_NAME.capitalize()}DetailView.as_view(), name="detail"),
            # path("new/",      views.{APP_NAME.capitalize()}CreateView.as_view(),  name="create"),
        ]
        """),

    os.path.join(BASE, "services.py"): textwrap.dedent(f"""\
        """
        \"\"\"
        {APP_NAME.capitalize()} business logic / service layer.

        Keep views thin — put complex query logic and business rules here.
        Services are plain Python functions/classes — easy to test without HTTP.
        \"\"\"
        import logging

        logger = logging.getLogger(__name__)
        """),

    os.path.join(BASE, "tasks.py"): textwrap.dedent(f"""\
        import logging

        from celery import shared_task

        logger = logging.getLogger(__name__)


        # @shared_task(bind=True, max_retries=3, default_retry_delay=60)
        # def example_task(self, item_id):
        #     try:
        #         logger.info("Processing item %s", item_id)
        #     except Exception as exc:
        #         raise self.retry(exc=exc)
        """),

    os.path.join(BASE, "signals.py"): textwrap.dedent(f"""\
        import logging

        # from django.db.models.signals import post_save
        # from django.dispatch import receiver
        # from .models import {APP_NAME.capitalize()}

        logger = logging.getLogger(__name__)

        # @receiver(post_save, sender={APP_NAME.capitalize()})
        # def on_{APP_NAME}_saved(sender, instance, created, **kwargs):
        #     if created:
        #         logger.debug("New {APP_NAME} created: %s", instance.pk)
        """),

    os.path.join(BASE, "api", "serializers.py"): textwrap.dedent(f"""\
        from rest_framework import serializers
        # from apps.{APP_NAME}.models import {APP_NAME.capitalize()}


        # class {APP_NAME.capitalize()}Serializer(serializers.ModelSerializer):
        #     class Meta:
        #         model  = {APP_NAME.capitalize()}
        #         fields = ("id", "name", "created_at", "updated_at")
        #         read_only_fields = ("id", "created_at", "updated_at")
        """),

    os.path.join(BASE, "api", "views.py"): textwrap.dedent(f"""\
        import logging

        from rest_framework import generics, permissions
        # from apps.{APP_NAME}.models import {APP_NAME.capitalize()}
        # from .serializers import {APP_NAME.capitalize()}Serializer

        logger = logging.getLogger(__name__)


        # class {APP_NAME.capitalize()}ListAPIView(generics.ListCreateAPIView):
        #     queryset           = {APP_NAME.capitalize()}.objects.all()
        #     serializer_class   = {APP_NAME.capitalize()}Serializer
        #     permission_classes = [permissions.IsAuthenticated]


        # class {APP_NAME.capitalize()}DetailAPIView(generics.RetrieveUpdateDestroyAPIView):
        #     queryset           = {APP_NAME.capitalize()}.objects.all()
        #     serializer_class   = {APP_NAME.capitalize()}Serializer
        #     permission_classes = [permissions.IsAuthenticated]
        """),

    os.path.join(BASE, "api", "urls.py"): textwrap.dedent(f"""\
        from django.urls import path
        from . import views

        app_name = "{APP_NAME}-api"

        urlpatterns = [
            # path("",          views.{APP_NAME.capitalize()}ListAPIView.as_view(),   name="list"),
            # path("<uuid:pk>/", views.{APP_NAME.capitalize()}DetailAPIView.as_view(), name="detail"),
        ]
        """),

    os.path.join(BASE, "tests", "test_models.py"): textwrap.dedent(f"""\
        import pytest

        # from apps.{APP_NAME}.models import {APP_NAME.capitalize()}


        # @pytest.mark.django_db
        # class Test{APP_NAME.capitalize()}Model:
        #     def test_str(self):
        #         obj = {APP_NAME.capitalize()}(name="Test")
        #         assert str(obj) == "Test"
        """),

    os.path.join(BASE, "tests", "test_api.py"): textwrap.dedent(f"""\
        import pytest
        from rest_framework import status
        from rest_framework.test import APIClient
        from django.contrib.auth import get_user_model

        User = get_user_model()


        @pytest.fixture
        def api_client():
            return APIClient()


        @pytest.fixture
        def auth_client(db):
            user = User.objects.create_user(email="test@example.com", password="pass123")
            client = APIClient()
            client.force_authenticate(user=user)
            return client

        # @pytest.mark.django_db
        # class Test{APP_NAME.capitalize()}API:
        #     list_url = "/api/v1/{APP_NAME}/"
        #
        #     def test_list_authenticated(self, auth_client):
        #         res = auth_client.get(self.list_url)
        #         assert res.status_code == status.HTTP_200_OK
        """),
}

def main():
    for d in DIRS:
        os.makedirs(d, exist_ok=True)

    for path, content in FILES.items():
        if not os.path.exists(path):
            with open(path, "w") as f:
                f.write(content)

    print(f"\n✓  App '{APP_NAME}' scaffolded at apps/{APP_NAME}/\n")
    print("  Next steps:\n")
    print(f"  1. Add to LOCAL_APPS in config/settings/base.py:")
    print(f'       "apps.{APP_NAME}",\n')
    print(f"  2. Add web routes in config/urls.py (inside urlpatterns):")
    print(f'       path("{APP_NAME}/", include("apps.{APP_NAME}.urls", namespace="{APP_NAME}")),\n')
    print(f"  3. Add API routes in config/urls.py (inside the api/v1/ group):")
    print(f'       path("{APP_NAME}/", include("apps.{APP_NAME}.api.urls", namespace="{APP_NAME}-api")),\n')
    print(f"  4. Define your models in apps/{APP_NAME}/models.py")
    print(f"  5. Run: python manage.py makemigrations {APP_NAME} && python manage.py migrate\n")


if __name__ == "__main__":
    main()
