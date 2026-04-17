"""
Template context processors.

Each function receives the request and returns a dict that is merged
into every template's context automatically.

Registered in settings/base.py under TEMPLATES → context_processors.
"""

from django.conf import settings


def site_settings(request):
    """
    Expose key site settings to every template.

    Usage in any template:
        {{ SITE_NAME }}
        {{ SITE_URL }}
        {{ SITE_TAGLINE }}
        {% if DEBUG %}...{% endif %}
    """
    return {
        "SITE_NAME":    getattr(settings, "SITE_NAME",    "MyProject"),
        "SITE_URL":     getattr(settings, "SITE_URL",     ""),
        "SITE_TAGLINE": getattr(settings, "SITE_TAGLINE", ""),
        "DEBUG":        settings.DEBUG,
    }
