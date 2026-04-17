"""
Custom template tags and filters.

Load in any template:
    {% load core_tags %}

    {{ user.bio|truncate_chars:100 }}
    {% active_link request "users:dashboard" %}
    {% url_with_params request page=2 %}
"""

from django import template
from django.urls import reverse, NoReverseMatch

register = template.Library()


# ─── Filters ──────────────────────────────────────────────────────────────────

@register.filter(name="truncate_chars")
def truncate_chars(value, max_length):
    """Truncate a string to max_length characters, adding ellipsis if needed."""
    value = str(value)
    if len(value) <= max_length:
        return value
    return value[:max_length - 1] + "…"


@register.filter(name="initials")
def initials(value):
    """Return initials from a full name: 'Alice Smith' → 'AS'."""
    parts = str(value).split()
    return "".join(p[0].upper() for p in parts if p)[:2]


@register.filter(name="file_size")
def file_size(value):
    """Format a byte count as a human-readable file size."""
    try:
        value = int(value)
    except (TypeError, ValueError):
        return "0 B"
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if value < 1024:
            return f"{value:.1f} {unit}"
        value /= 1024
    return f"{value:.1f} PB"


# ─── Tags ─────────────────────────────────────────────────────────────────────

@register.simple_tag(takes_context=True)
def active_link(context, url_name, css_class="active"):
    """
    Return css_class if the current URL matches url_name, else empty string.

    Usage:
        <a href="{% url 'users:dashboard' %}"
           class="nav-link {% active_link request 'users:dashboard' %}">
          Dashboard
        </a>
    """
    request = context.get("request")
    if not request:
        return ""
    try:
        pattern = reverse(url_name)
    except NoReverseMatch:
        return ""
    return css_class if request.path.startswith(pattern) else ""


@register.simple_tag(takes_context=True)
def url_with_params(context, **kwargs):
    """
    Return current URL with updated/added query params.

    Usage:  <a href="{% url_with_params request page=2 %}">Next</a>
    """
    request = context.get("request")
    if not request:
        return ""
    params = request.GET.copy()
    for key, value in kwargs.items():
        params[key] = value
    return f"{request.path}?{params.urlencode()}"
