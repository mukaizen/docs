from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

User = get_user_model()


class UserPublicSerializer(serializers.ModelSerializer):
    """Minimal public-safe representation of a user."""
    display_name = serializers.CharField(read_only=True)
    avatar_url   = serializers.CharField(read_only=True)

    class Meta:
        model  = User
        fields = ("id", "display_name", "avatar_url", "date_joined")
        read_only_fields = fields


class UserProfileSerializer(serializers.ModelSerializer):
    """Full profile — returned to the authenticated user for their own account."""
    display_name = serializers.CharField(read_only=True)
    avatar_url   = serializers.CharField(read_only=True)

    class Meta:
        model  = User
        fields = (
            "id", "email", "first_name", "last_name",
            "display_name", "avatar", "avatar_url",
            "bio", "phone", "timezone", "website",
            "is_email_verified", "date_joined",
            "created_at", "updated_at",
        )
        read_only_fields = (
            "id", "email", "is_email_verified",
            "date_joined", "created_at", "updated_at",
        )


class UserProfileUpdateSerializer(serializers.ModelSerializer):
    """Only the fields a user can update on their own profile."""
    class Meta:
        model  = User
        fields = ("first_name", "last_name", "avatar", "bio", "phone", "timezone", "website")

    def validate_avatar(self, value):
        if value and value.size > 5 * 1024 * 1024:
            raise serializers.ValidationError(_("Avatar must be smaller than 5 MB."))
        return value


class RegisterSerializer(serializers.ModelSerializer):
    password  = serializers.CharField(write_only=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, label=_("Confirm password"))

    class Meta:
        model  = User
        fields = ("email", "first_name", "last_name", "password", "password2")

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError({"password": _("Passwords do not match.")})
        return attrs

    def validate_email(self, value):
        if User.objects.filter(email=value.lower()).exists():
            raise serializers.ValidationError(_("An account with this email already exists."))
        return value.lower()

    def create(self, validated_data):
        validated_data.pop("password2")
        return User.objects.create_user(**validated_data)


class ChangePasswordSerializer(serializers.Serializer):
    old_password  = serializers.CharField(write_only=True)
    new_password  = serializers.CharField(write_only=True, validators=[validate_password])
    new_password2 = serializers.CharField(write_only=True)

    def validate(self, attrs):
        if attrs["new_password"] != attrs["new_password2"]:
            raise serializers.ValidationError({"new_password": _("Passwords do not match.")})
        return attrs

    def validate_old_password(self, value):
        user = self.context["request"].user
        if not user.check_password(value):
            raise serializers.ValidationError(_("Current password is incorrect."))
        return value

    def save(self, **kwargs):
        user = self.context["request"].user
        user.set_password(self.validated_data["new_password"])
        user.save(update_fields=["password"])
        return user
