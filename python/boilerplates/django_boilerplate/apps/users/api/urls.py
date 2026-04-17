"""
Users API URL configuration.
All routes are prefixed with /api/v1/users/ (set in config/urls.py).

Endpoints:
  POST   /api/v1/users/register/            → create account + return token
  POST   /api/v1/users/login/               → get token
  POST   /api/v1/users/logout/              → delete token
  GET    /api/v1/users/me/                  → own profile
  PATCH  /api/v1/users/me/                  → update own profile
  POST   /api/v1/users/me/change-password/  → change password
  GET    /api/v1/users/<uuid:pk>/           → public profile
"""

from django.urls import path
from .views import (
    RegisterAPIView,
    LoginAPIView,
    LogoutAPIView,
    MeAPIView,
    ChangePasswordAPIView,
    UserPublicDetailAPIView,
)

app_name = "users-api"

urlpatterns = [
    path("register/",            RegisterAPIView.as_view(),        name="register"),
    path("login/",               LoginAPIView.as_view(),           name="login"),
    path("logout/",              LogoutAPIView.as_view(),          name="logout"),
    path("me/",                  MeAPIView.as_view(),              name="me"),
    path("me/change-password/",  ChangePasswordAPIView.as_view(),  name="change-password"),
    path("<uuid:pk>/",           UserPublicDetailAPIView.as_view(), name="public-profile"),
]
