"""
Core utility views.

health_check — used by load balancers / uptime monitors
error handlers — 400, 403, 404, 500 registered in config/urls.py
"""

import logging

from django.http import JsonResponse
from django.shortcuts import render

logger = logging.getLogger(__name__)


# ─── Health Check ─────────────────────────────────────────────────────────────

def health_check(request):
    """
    GET /core/health/
    Returns 200 OK with DB connectivity status.
    Used by Docker HEALTHCHECK, load balancers, and uptime monitors (UptimeRobot etc.)
    """
    from django.db import connection
    try:
        connection.ensure_connection()
        db_ok = True
    except Exception:
        db_ok = False

    payload = {
        "status": "ok" if db_ok else "degraded",
        "db":     "ok" if db_ok else "error",
    }
    status_code = 200 if db_ok else 503
    return JsonResponse(payload, status=status_code)


# ─── Error Handlers ───────────────────────────────────────────────────────────
# To activate, add to config/urls.py:
#   handler400 = "apps.core.views.bad_request"
#   handler403 = "apps.core.views.permission_denied"
#   handler404 = "apps.core.views.page_not_found"
#   handler500 = "apps.core.views.server_error"

def bad_request(request, exception=None):
    logger.warning("400 Bad Request: %s", request.path)
    return render(request, "errors/400.html", status=400)


def permission_denied(request, exception=None):
    logger.warning("403 Forbidden: %s — user: %s", request.path, request.user)
    return render(request, "errors/403.html", status=403)


def page_not_found(request, exception=None):
    logger.info("404 Not Found: %s", request.path)
    return render(request, "errors/404.html", status=404)


def server_error(request):
    logger.error("500 Server Error: %s", request.path)
    return render(request, "errors/500.html", status=500)
