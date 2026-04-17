"""
Development settings.
Run with:  DJANGO_SETTINGS_MODULE=config.settings.development
Or simply: python manage.py runserver   (manage.py defaults to this)
"""

from .base import *  # noqa: F401, F403

DEBUG = True

ALLOWED_HOSTS = ["*"]

# ─── Dev-only apps ────────────────────────────────────────────────────────────
INSTALLED_APPS += [  # noqa: F405
    "debug_toolbar",
]

MIDDLEWARE += [  # noqa: F405
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

INTERNAL_IPS = ["127.0.0.1"]

# ─── Database: SQLite for local dev (override with .env if you prefer Postgres)
# Set DATABASE_URL=sqlite:///db.sqlite3 in .env or leave blank for this default

# ─── Email: Print to console in dev ───────────────────────────────────────────
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# ─── Cache: Dummy cache (no Redis needed locally) ─────────────────────────────
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.dummy.DummyCache",
    }
}

# ─── Celery: run tasks synchronously in dev (no worker needed) ─────────────
CELERY_TASK_ALWAYS_EAGER = True
CELERY_TASK_EAGER_PROPAGATES = True

# ─── CORS: allow everything in dev ───────────────────────────────────────────
CORS_ALLOW_ALL_ORIGINS = True

# ─── DRF: add browsable API renderer in dev ──────────────────────────────────
REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] += [  # noqa: F405
    "rest_framework.renderers.BrowsableAPIRenderer",
]

# ─── Debug toolbar panels ────────────────────────────────────────────────────
DEBUG_TOOLBAR_PANELS = [
    "debug_toolbar.panels.history.HistoryPanel",
    "debug_toolbar.panels.versions.VersionsPanel",
    "debug_toolbar.panels.timer.TimerPanel",
    "debug_toolbar.panels.settings.SettingsPanel",
    "debug_toolbar.panels.headers.HeadersPanel",
    "debug_toolbar.panels.request.RequestPanel",
    "debug_toolbar.panels.sql.SQLPanel",
    "debug_toolbar.panels.staticfiles.StaticFilesPanel",
    "debug_toolbar.panels.templates.TemplatesPanel",
    "debug_toolbar.panels.cache.CachePanel",
    "debug_toolbar.panels.signals.SignalsPanel",
    "debug_toolbar.panels.logging.LoggingPanel",
    "debug_toolbar.panels.profiling.ProfilingPanel",
]

# ─── Logging: verbose in dev ─────────────────────────────────────────────────
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {"class": "logging.StreamHandler"},
    },
    "root": {
        "handlers": ["console"],
        "level": "DEBUG",
    },
    "loggers": {
        "django.db.backends": {
            "handlers": ["console"],
            "level": "DEBUG",   # logs every SQL query
            "propagate": False,
        },
    },
}
