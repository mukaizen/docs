"""
Test settings — fast, isolated, no external deps.
Run with:  pytest  (pytest.ini sets DJANGO_SETTINGS_MODULE automatically)
"""

from .base import *  # noqa: F401, F403

DEBUG = False

# ─── Faster password hashing in tests ────────────────────────────────────────
PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.MD5PasswordHasher",
]

# ─── In-memory SQLite for fast tests ─────────────────────────────────────────
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
        "ATOMIC_REQUESTS": True,
    }
}

# ─── No real emails ───────────────────────────────────────────────────────────
EMAIL_BACKEND = "django.core.mail.backends.locmem.EmailBackend"

# ─── No cache ────────────────────────────────────────────────────────────────
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache",
    }
}

# ─── Celery eager in tests ────────────────────────────────────────────────────
CELERY_TASK_ALWAYS_EAGER    = True
CELERY_TASK_EAGER_PROPAGATES = True

# ─── Static files — no manifest needed ───────────────────────────────────────
STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"

# ─── Media files — temp dir ───────────────────────────────────────────────────
import tempfile  # noqa: E402
MEDIA_ROOT = tempfile.mkdtemp()

DEFAULT_FROM_EMAIL = "test@example.com"
