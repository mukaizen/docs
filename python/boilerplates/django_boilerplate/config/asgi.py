"""
ASGI config — used by Daphne / Uvicorn for async support (WebSockets, etc.).

Deploy with:
  uvicorn config.asgi:application --host 0.0.0.0 --port 8000 --workers 4
"""
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")
application = get_asgi_application()
