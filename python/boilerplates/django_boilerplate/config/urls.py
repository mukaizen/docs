"""
Root URL configuration.

How to add a new app:
─────────────────────
1. Create your app:        python manage.py startapp apps/myapp
2. Add to INSTALLED_APPS:  "apps.myapp" in config/settings/base.py
3. Create apps/myapp/urls.py with your urlpatterns
4. Include below:          path("myapp/", include("apps.myapp.urls", namespace="myapp"))

URL namespacing convention:
  - API routes:   /api/v1/<app>/
  - Web routes:   /<app>/
  - Admin:        /<ADMIN_URL>/   (randomised in production)
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import RedirectView

# In production, ADMIN_URL is a secret path from .env (e.g. "x7k2m-admin/")
admin_url = getattr(settings, "ADMIN_URL", "admin/")

urlpatterns = [
    # Admin
    path(admin_url, admin.site.urls),

    # Web App Routes
    path("", RedirectView.as_view(url="/dashboard/", permanent=False), name="home"),
    path("users/", include("apps.users.urls", namespace="users")),

    # API Routes
    path("api/v1/", include([
        path("users/", include("apps.users.api.urls", namespace="users-api")),
        # ADD NEW APP API ROUTES HERE:
        # path("blog/",  include("apps.blog.api.urls",  namespace="blog-api")),
        # path("shop/",  include("apps.shop.api.urls",  namespace="shop-api")),
    ])),

    # Core / Utility
    path("core/", include("apps.core.urls", namespace="core")),
]

# Debug Toolbar
if settings.DEBUG:
    urlpatterns += [path("__debug__/", include("debug_toolbar.urls"))]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
