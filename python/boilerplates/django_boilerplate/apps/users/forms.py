from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext_lazy as _

User = get_user_model()


# ─── Admin Forms ──────────────────────────────────────────────────────────────

class CustomUserCreationForm(UserCreationForm):
    """Used in Django admin to create a new user."""
    class Meta(UserCreationForm.Meta):
        model  = User
        fields = ("email", "first_name", "last_name")


class CustomUserChangeForm(UserChangeForm):
    """Used in Django admin to edit a user."""
    class Meta(UserChangeForm.Meta):
        model  = User
        fields = ("email", "first_name", "last_name")


# ─── Public-facing Forms ──────────────────────────────────────────────────────

class RegisterForm(UserCreationForm):
    email      = forms.EmailField(label=_("Email"), widget=forms.EmailInput(attrs={"autofocus": True}))
    first_name = forms.CharField(label=_("First name"), max_length=150)
    last_name  = forms.CharField(label=_("Last name"),  max_length=150)

    class Meta:
        model  = User
        fields = ("email", "first_name", "last_name", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data["email"].lower()
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(_("An account with this email already exists."))
        return email


class ProfileUpdateForm(forms.ModelForm):
    """Let users update their own profile."""
    class Meta:
        model  = User
        fields = ("first_name", "last_name", "avatar", "bio", "phone", "timezone", "website")
        widgets = {
            "bio": forms.Textarea(attrs={"rows": 4}),
        }

    def clean_avatar(self):
        avatar = self.cleaned_data.get("avatar")
        if avatar and avatar.size > 5 * 1024 * 1024:  # 5 MB limit
            raise forms.ValidationError(_("Avatar file too large (max 5 MB)."))
        return avatar


class EmailChangeForm(forms.Form):
    email    = forms.EmailField(label=_("New email address"))
    password = forms.CharField(label=_("Current password"), widget=forms.PasswordInput)

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean_email(self):
        email = self.cleaned_data["email"].lower()
        if User.objects.exclude(pk=self.user.pk).filter(email=email).exists():
            raise forms.ValidationError(_("That email is already in use."))
        return email

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if not self.user.check_password(password):
            raise forms.ValidationError(_("Incorrect password."))
        return password
