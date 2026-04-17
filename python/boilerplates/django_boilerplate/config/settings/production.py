"""
Production settings.
Run with:  DJANGO_SETTINGS_MODULE=config.settings.production

All sensitive values MUST come from environment variables — never hardcoded.
"""

from .base import *  # noqa: F401, F403

DEBUG = False

ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS")  # noqa: F405

# ─── Security headers ─────────────────────────────────────────────────────────
SECURE_PROXY_SSL_HEADER      = ("HTTP_X_FORWARDED_PROTO", "https")
SECURE_SSL_REDIRECT           = True
SESSION_COOKIE_SECURE         = True
CSRF_COOKIE_SECURE            = True
SECURE_HSTS_SECONDS           = 31536000   # 1 year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD           = True
SECURE_CONTENT_TYPE_NOSNIFF   = True
SECURE_BROWSER_XSS_FILTER     = True
X_FRAME_OPTIONS               = "DENY"
CSRF_COOKIE_HTTPONLY          = True

# ─── Email via SMTP ───────────────────────────────────────────────────────────
EMAIL_BACKEND  = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST     = env("EMAIL_HOST")  # noqa: F405
EMAIL_PORT     = env.int("EMAIL_PORT", default=587)  # noqa: F405
EMAIL_USE_TLS  = env.bool("EMAIL_USE_TLS", default=True)  # noqa: F405
EMAIL_HOST_USER     = env("EMAIL_HOST_USER")  # noqa: F405
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD")  # noqa: F405

# ─── Static / Media — S3 (optional, comment out to use whitenoise/local) ──────
# Uncomment this block to serve files via AWS S3 / DigitalOcean Spaces / etc.
#
# INSTALLED_APPS += ["storages"]  # noqa: F405
# AWS_ACCESS_KEY_ID       = env("AWS_ACCESS_KEY_ID")
# AWS_SECRET_ACCESS_KEY   = env("AWS_SECRET_ACCESS_KEY")
# AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME")
# AWS_S3_REGION_NAME      = env("AWS_S3_REGION_NAME", default="us-east-1")
# AWS_S3_CUSTOM_DOMAIN    = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
# AWS_DEFAULT_ACL         = "public-read"
# AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400"}
#
# STATIC_URL  = f"https://{AWS_S3_CUSTOM_DOMAIN}/static/"
# MEDIA_URL   = f"https://{AWS_S3_CUSTOM_DOMAIN}/media/"
# DEFAULT_FILE_STORAGE    = "config.storage_backends.MediaStorage"
# STATICFILES_STORAGE     = "config.storage_backends.StaticStorage"

# ─── Logging ─────────────────────────────────────────────────────────────────
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} {process:d} {thread:d} {message}",
            "style": "{",
        },
        "json": {
            "()": "pythonjsonlogger.jsonlogger.JsonFormatter",
            "format": "%(asctime)s %(name)s %(levelname)s %(message)s",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        "file": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": BASE_DIR / "logs/django.log",  # noqa: F405
            "maxBytes": 1024 * 1024 * 10,  # 10 MB
            "backupCount": 5,
            "formatter": "verbose",
        },
    },
    "root": {
        "handlers": ["console", "file"],
        "level": "INFO",
    },
    "loggers": {
        "django": {
            "handlers": ["console", "file"],
            "level": "INFO",
            "propagate": False,
        },
        "django.security": {
            "handlers": ["console", "file"],
            "level": "WARNING",
            "propagate": False,
        },
    },
}

# ─── Admin URL — randomise in production to reduce attack surface ─────────────
ADMIN_URL = env("DJANGO_ADMIN_URL", default="admin/")  # noqa: F405
