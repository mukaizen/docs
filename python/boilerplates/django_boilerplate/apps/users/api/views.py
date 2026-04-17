import logging

from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import (
    ChangePasswordSerializer,
    RegisterSerializer,
    UserProfileSerializer,
    UserProfileUpdateSerializer,
    UserPublicSerializer,
)

User = get_user_model()
logger = logging.getLogger(__name__)


class RegisterAPIView(generics.CreateAPIView):
    """
    POST /api/v1/users/register/
    Create a new user account. Returns auth token on success.
    """
    serializer_class   = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user  = serializer.save()
        token, _ = Token.objects.get_or_create(user=user)
        logger.info("API: New user registered %s", user.email)
        return Response(
            {"token": token.key, "user": UserProfileSerializer(user).data},
            status=status.HTTP_201_CREATED,
        )


class LoginAPIView(ObtainAuthToken):
    """
    POST /api/v1/users/login/
    Body: { "username": "<email>", "password": "<password>" }
    Returns auth token + user profile.
    """
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user  = serializer.validated_data["user"]
        token, _ = Token.objects.get_or_create(user=user)
        logger.info("API: User logged in %s", user.email)
        return Response({
            "token": token.key,
            "user":  UserProfileSerializer(user).data,
        })


class LogoutAPIView(APIView):
    """
    POST /api/v1/users/logout/
    Deletes the auth token, invalidating all sessions for this token.
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        try:
            request.user.auth_token.delete()
        except Token.DoesNotExist:
            pass
        logger.info("API: User logged out %s", request.user.email)
        return Response({"detail": "Successfully logged out."}, status=status.HTTP_200_OK)


class MeAPIView(generics.RetrieveUpdateAPIView):
    """
    GET  /api/v1/users/me/  → return own profile
    PATCH /api/v1/users/me/ → update own profile (partial)
    """
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method in ("PUT", "PATCH"):
            return UserProfileUpdateSerializer
        return UserProfileSerializer

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        kwargs["partial"] = True   # always partial — PATCH semantics
        return super().update(request, *args, **kwargs)


class ChangePasswordAPIView(generics.GenericAPIView):
    """
    POST /api/v1/users/me/change-password/
    Body: { "old_password", "new_password", "new_password2" }
    """
    serializer_class   = ChangePasswordSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # Invalidate old token so user must re-login
        Token.objects.filter(user=request.user).delete()
        return Response({"detail": "Password changed. Please log in again."})


class UserPublicDetailAPIView(generics.RetrieveAPIView):
    """
    GET /api/v1/users/<uuid:pk>/
    Public profile — limited fields only.
    """
    queryset           = User.objects.active()
    serializer_class   = UserPublicSerializer
    permission_classes = [permissions.AllowAny]
