"""
Tests for the users app.
Run:  pytest apps/users/
"""

import pytest
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

User = get_user_model()


# ─── Fixtures ─────────────────────────────────────────────────────────────────

@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def user(db):
    return User.objects.create_user(
        email="alice@example.com",
        first_name="Alice",
        last_name="Smith",
        password="StrongPass123!",
    )


@pytest.fixture
def auth_client(api_client, user):
    api_client.force_authenticate(user=user)
    return api_client


# ─── Model Tests ──────────────────────────────────────────────────────────────

@pytest.mark.django_db
class TestUserModel:
    def test_create_user(self):
        user = User.objects.create_user(
            email="bob@example.com",
            password="pass",
            first_name="Bob",
            last_name="Jones",
        )
        assert user.email == "bob@example.com"
        assert user.check_password("pass")
        assert user.is_active
        assert not user.is_staff

    def test_create_superuser(self):
        admin = User.objects.create_superuser(email="admin@example.com", password="pass")
        assert admin.is_staff
        assert admin.is_superuser

    def test_display_name_with_names(self, user):
        assert user.display_name == "Alice Smith"

    def test_display_name_fallback(self):
        user = User.objects.create_user(email="nnn@example.com", password="pass")
        assert user.display_name == "nnn"  # email prefix

    def test_str_is_email(self, user):
        assert str(user) == "alice@example.com"


# ─── API: Register ─────────────────────────────────────────────────────────────

@pytest.mark.django_db
class TestRegisterAPI:
    url = "/api/v1/users/register/"

    def test_register_success(self, api_client):
        payload = {
            "email": "new@example.com",
            "first_name": "New",
            "last_name": "User",
            "password": "StrongPass123!",
            "password2": "StrongPass123!",
        }
        res = api_client.post(self.url, payload)
        assert res.status_code == status.HTTP_201_CREATED
        assert "token" in res.data
        assert User.objects.filter(email="new@example.com").exists()

    def test_register_duplicate_email(self, api_client, user):
        payload = {
            "email": "alice@example.com",
            "first_name": "A", "last_name": "B",
            "password": "StrongPass123!", "password2": "StrongPass123!",
        }
        res = api_client.post(self.url, payload)
        assert res.status_code == status.HTTP_400_BAD_REQUEST

    def test_register_passwords_mismatch(self, api_client):
        payload = {
            "email": "x@example.com",
            "first_name": "X", "last_name": "Y",
            "password": "StrongPass123!", "password2": "Different123!",
        }
        res = api_client.post(self.url, payload)
        assert res.status_code == status.HTTP_400_BAD_REQUEST


# ─── API: Me ──────────────────────────────────────────────────────────────────

@pytest.mark.django_db
class TestMeAPI:
    url = "/api/v1/users/me/"

    def test_get_profile_authenticated(self, auth_client, user):
        res = auth_client.get(self.url)
        assert res.status_code == status.HTTP_200_OK
        assert res.data["email"] == user.email

    def test_get_profile_unauthenticated(self, api_client):
        res = api_client.get(self.url)
        assert res.status_code == status.HTTP_401_UNAUTHORIZED

    def test_update_profile(self, auth_client):
        res = auth_client.patch(self.url, {"first_name": "Updated", "bio": "Hello"})
        assert res.status_code == status.HTTP_200_OK
        assert res.data["first_name"] == "Updated"


# ─── API: Change Password ─────────────────────────────────────────────────────

@pytest.mark.django_db
class TestChangePasswordAPI:
    url = "/api/v1/users/me/change-password/"

    def test_change_password_success(self, auth_client, user):
        res = auth_client.post(self.url, {
            "old_password": "StrongPass123!",
            "new_password": "NewStrongPass456!",
            "new_password2": "NewStrongPass456!",
        })
        assert res.status_code == status.HTTP_200_OK
        user.refresh_from_db()
        assert user.check_password("NewStrongPass456!")

    def test_change_password_wrong_old(self, auth_client):
        res = auth_client.post(self.url, {
            "old_password": "wrong",
            "new_password": "NewStrongPass456!",
            "new_password2": "NewStrongPass456!",
        })
        assert res.status_code == status.HTTP_400_BAD_REQUEST
