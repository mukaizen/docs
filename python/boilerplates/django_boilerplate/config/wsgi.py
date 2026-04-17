"""
WSGI config — used by Gunicorn in production.

Deploy with:
  gunicorn config.wsgi:application --workers 4 --bind 0.0.0.0:8000

Set DJANGO_SETTINGS_MODULE in your process manager / Docker ENV.
"""
import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")
application = get_wsgi_application()
