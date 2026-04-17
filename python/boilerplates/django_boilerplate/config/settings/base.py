"""
Base settings — shared across all environments.
Do NOT use this file directly. Use development.py or production.py.

Environment variables are loaded via django-environ.
Copy .env.example → .env and fill in values.
"""

from pathlib import Path
import environ

# ─── Paths ────────────────────────────────────────────────────────────────────
# BASE_DIR = /path/to/project  (where manage.py lives)
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# ─── Environment ──────────────────────────────────────────────────────────────
env = environ.Env()
environ.Env.read_env(BASE_DIR / ".env")

# ─── Security ─────────────────────────────────────────────────────────────────
SECRET_KEY = env("DJANGO_SECRET_KEY")
DEBUG = env.bool("DJANGO_DEBUG", default=False)
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=[])

# ─── Application Definition ───────────────────────────────────────────────────
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
]

THIRD_PARTY_APPS = [
    "rest_framework",
    "rest_framework.authtoken",
    "corsheaders",
]

# ┌─────────────────────────────────────────────────────────────────────────────┐
# │  ADD YOUR APPS HERE                                                          │
# │  Convention: all custom apps live in apps/                                  │
# │  Example:  "apps.blog"  |  "apps.shop"  |  "apps.notifications"            │
# └─────────────────────────────────────────────────────────────────────────────┘
LOCAL_APPS = [
    "apps.core",    # Shared utilities, mixins, base models
    "apps.users",   # Custom user model + profiles
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# ─── Middleware ───────────────────────────────────────────────────────────────
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",   # static files in production
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ─── URLs ─────────────────────────────────────────────────────────────────────
ROOT_URLCONF = "config.urls"

# ─── Templates ────────────────────────────────────────────────────────────────
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # Global templates folder — app templates go in apps/<name>/templates/
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                # Project-wide context available in every template
                "apps.core.context_processors.site_settings",
            ],
        },
    },
]

# ─── WSGI / ASGI ──────────────────────────────────────────────────────────────
WSGI_APPLICATION = "config.wsgi.application"
ASGI_APPLICATION  = "config.asgi.application"

# ─── Database ─────────────────────────────────────────────────────────────────
# Reads DATABASE_URL from .env  e.g.  postgres://user:pass@host:5432/dbname
DATABASES = {
    "default": env.db("DATABASE_URL", default=f"sqlite:///{BASE_DIR}/db.sqlite3")
}
DATABASES["default"]["ATOMIC_REQUESTS"] = True  # wrap each request in a transaction

# ─── Authentication ───────────────────────────────────────────────────────────
AUTH_USER_MODEL = "users.User"          # our custom user model

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
]

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
     "OPTIONS": {"min_length": 8}},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LOGIN_URL          = "/users/login/"
LOGIN_REDIRECT_URL = "/dashboard/"
LOGOUT_REDIRECT_URL = "/"

# ─── Internationalisation ─────────────────────────────────────────────────────
LANGUAGE_CODE = "en-us"
TIME_ZONE     = env("DJANGO_TIMEZONE", default="UTC")
USE_I18N      = True
USE_TZ        = True

# ─── Static & Media Files ─────────────────────────────────────────────────────
STATIC_URL  = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"          # collected here for deployment
STATICFILES_DIRS = [BASE_DIR / "static"]        # source static files

MEDIA_URL  = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# WhiteNoise compression for static files
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# ─── Default Primary Key ──────────────────────────────────────────────────────
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ─── Django REST Framework ────────────────────────────────────────────────────
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_PAGINATION_CLASS": "apps.core.pagination.StandardResultsPagination",
    "PAGE_SIZE": 20,
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
    "DEFAULT_THROTTLE_CLASSES": [
        "rest_framework.throttling.AnonRateThrottle",
        "rest_framework.throttling.UserRateThrottle",
    ],
    "DEFAULT_THROTTLE_RATES": {
        "anon": "100/day",
        "user": "1000/day",
    },
}

# ─── CORS ─────────────────────────────────────────────────────────────────────
CORS_ALLOWED_ORIGINS = env.list("CORS_ALLOWED_ORIGINS", default=[])
CORS_ALLOW_CREDENTIALS = True

# ─── Email ────────────────────────────────────────────────────────────────────
DEFAULT_FROM_EMAIL = env("DEFAULT_FROM_EMAIL", default="noreply@example.com")
SERVER_EMAIL       = env("SERVER_EMAIL", default="server@example.com")

# ─── Celery ───────────────────────────────────────────────────────────────────
CELERY_BROKER_URL        = env("CELERY_BROKER_URL", default="redis://localhost:6379/0")
CELERY_RESULT_BACKEND    = env("CELERY_RESULT_BACKEND", default="redis://localhost:6379/0")
CELERY_ACCEPT_CONTENT    = ["json"]
CELERY_TASK_SERIALIZER   = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TIMEZONE          = TIME_ZONE

# ─── Cache ────────────────────────────────────────────────────────────────────
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.redis.RedisCache",
        "LOCATION": env("REDIS_URL", default="redis://localhost:6379/1"),
    }
}

# ─── Sessions ─────────────────────────────────────────────────────────────────
SESSION_ENGINE         = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS    = "default"
SESSION_COOKIE_AGE     = 60 * 60 * 24 * 14   # 2 weeks
SESSION_COOKIE_HTTPONLY = True

# ─── Site-wide Settings ───────────────────────────────────────────────────────
# Available in templates via: {{ SITE_NAME }}
SITE_NAME    = env("SITE_NAME", default="MyProject")
SITE_URL     = env("SITE_URL", default="http://localhost:8000")
SITE_TAGLINE = env("SITE_TAGLINE", default="")
