"""
Celery application configuration.

Usage:
  Start worker:    celery -A config.celery_app worker -l info
  Start beat:      celery -A config.celery_app beat -l info
  Monitor (Flower):celery -A config.celery_app flower

Scheduled tasks are defined in CELERY_BEAT_SCHEDULE (add to base.py).
"""

import os

from celery import Celery

# Default to development settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")

app = Celery("config")

# Read config from Django settings, namespace CELERY_
app.config_from_object("django.conf:settings", namespace="CELERY")

# Auto-discover tasks.py in every INSTALLED_APP
app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f"Request: {self.request!r}")
