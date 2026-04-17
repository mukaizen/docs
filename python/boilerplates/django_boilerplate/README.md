# 🐍 Django Production Boilerplate

A production-ready Django project template built for real-world projects.
Includes a custom User model, REST API, Celery, Docker, CI/CD, and clear
patterns for adding new apps without guesswork.

---

## Table of Contents

1. [Features](#features)
2. [Project Structure](#project-structure)
3. [Quick Start](#quick-start)
4. [Settings Explained](#settings-explained)
5. [Environment Variables](#environment-variables)
6. [Adding a New App](#adding-a-new-app)
7. [URL Routing](#url-routing)
8. [Users App](#users-app)
9. [REST API](#rest-api)
10. [Celery Tasks](#celery-tasks)
11. [Running Tests](#running-tests)
12. [Docker](#docker)
13. [Production Deployment](#production-deployment)
14. [Code Quality](#code-quality)

---

## Features

| Feature | Implementation |
|---|---|
| Custom User model | Email-based auth, UUID pk, avatar, bio, timezone |
| Split settings | `base` / `development` / `production` / `testing` |
| REST API | Django REST Framework + Token auth |
| Async tasks | Celery + Redis |
| Static files | WhiteNoise (dev & prod), optional S3 |
| Database | PostgreSQL (SQLite for local dev) |
| Containerised | Docker + Docker Compose |
| CI/CD | GitHub Actions |
| Testing | pytest + pytest-django + factory-boy |
| Linting | ruff (lint + format) |
| Security | HSTS, CSP headers, secret admin URL, env-only secrets |
| New app scaffold | `make newapp name=blog` or `python scripts/new_app.py blog` |

---

## Project Structure

```
myproject/
│
├── apps/                          # All custom Django apps live here
│   ├── core/                      # Shared utilities (base models, mixins, pagination)
│   │   ├── models.py              # TimeStampedModel, UUIDModel, SoftDeleteModel, SingletonModel
│   │   ├── mixins.py              # View mixins: StaffRequired, OwnerRequired, etc.
│   │   ├── pagination.py          # DRF pagination classes
│   │   ├── context_processors.py  # SITE_NAME, SITE_URL in every template
│   │   ├── templatetags/
│   │   │   └── core_tags.py       # {% active_link %}, {{ value|truncate_chars:100 }}
│   │   └── views.py               # health_check + error handlers (400/403/404/500)
│   │
│   └── users/                     # Custom User model + profile + auth
│       ├── models.py              # User (email auth, UUID pk, avatar, bio, phone…)
│       ├── managers.py            # UserManager (create_user, create_superuser)
│       ├── views.py               # Register, Login, Profile, Settings, Delete
│       ├── forms.py               # RegisterForm, ProfileUpdateForm, EmailChangeForm
│       ├── urls.py                # Web routes for users app
│       ├── admin.py               # Custom UserAdmin
│       ├── signals.py             # Auto-create auth token on user create
│       ├── tasks.py               # send_welcome_email_task, send_email_verification_task
│       ├── tests.py               # Model + API tests
│       └── api/
│           ├── serializers.py     # UserPublic, UserProfile, Register, ChangePassword
│           ├── views.py           # Register, Login, Logout, Me, ChangePassword API
│           └── urls.py            # /api/v1/users/* routes
│
├── config/                        # Project configuration (not an app)
│   ├── settings/
│   │   ├── base.py                # Shared settings (loaded by all environments)
│   │   ├── development.py         # DEBUG=True, console email, dummy cache, toolbar
│   │   ├── production.py          # HTTPS, HSTS, SMTP, logging
│   │   └── testing.py             # In-memory DB, fast hasher, no email
│   ├── urls.py                    # Root URL conf — include app URLs here
│   ├── celery_app.py              # Celery configuration
│   ├── wsgi.py                    # WSGI entry point (Gunicorn)
│   └── asgi.py                    # ASGI entry point (Uvicorn / Daphne)
│
├── templates/                     # Global templates
│   ├── base.html                  # Root layout — all pages extend this
│   ├── partials/
│   │   ├── _navbar.html
│   │   └── _footer.html
│   ├── users/                     # User app templates
│   ├── emails/                    # HTML email templates
│   └── errors/                    # 400 / 403 / 404 / 500 error pages
│
├── static/                        # Source static files (collected to staticfiles/)
│   ├── css/main.css
│   └── js/main.js
│
├── requirements/
│   ├── base.txt                   # Shared deps (all environments)
│   ├── development.txt            # + debug toolbar, pytest, ruff
│   ├── production.txt             # + gunicorn, sentry
│   └── testing.txt                # + pytest only (for CI)
│
├── scripts/
│   └── new_app.py                 # Scaffold a new app: python scripts/new_app.py blog
│
├── docs/
│   └── nginx.conf                 # Production Nginx config with SSL
│
├── .env.example                   # Template for environment variables
├── .gitignore
├── .pre-commit-config.yaml        # pre-commit hooks (ruff, secret detection)
├── pyproject.toml                 # ruff configuration
├── pytest.ini                     # pytest configuration
├── Makefile                       # Dev commands (make dev, make test, make newapp…)
├── Dockerfile                     # Multi-stage production Docker image
├── docker-compose.yml             # Full local dev stack
└── README.md
```

---

## Quick Start

### Option A — Local (no Docker)

```bash
# 1. Clone and enter the project
git clone <your-repo-url> myproject
cd myproject

# 2. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 3. Install dev dependencies + copy .env
make install                     # runs: pip install -r requirements/development.txt
                                 #        pre-commit install
                                 #        cp .env.example .env  (if .env missing)

# 4. Fill in your .env (minimum: DJANGO_SECRET_KEY)
#    Generate a key:
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

# 5. Run migrations
make migrate

# 6. Create a superuser
make superuser

# 7. Start the dev server
make dev
# → http://localhost:8000
# → http://localhost:8000/admin/
```

### Option B — Docker (recommended)

```bash
# 1. Copy .env
cp .env.example .env
# Edit .env — set DJANGO_SECRET_KEY at minimum

# 2. Start the full stack (web + postgres + redis + celery)
make docker-up

# 3. Run migrations (in a second terminal)
make docker-migrate

# 4. Create superuser
make docker-superuser

# → http://localhost:8000
```

---

## Settings Explained

Settings are split into four files so you never accidentally run production
code with DEBUG=True, or leak secrets in version control.

```
config/settings/
  base.py          ← Shared by everything. No secrets here.
  development.py   ← extends base. DEBUG=True, console email, dummy cache.
  production.py    ← extends base. HTTPS, HSTS, SMTP, file logging.
  testing.py       ← extends base. In-memory SQLite, fast hasher.
```

**Which file is active?** Set the `DJANGO_SETTINGS_MODULE` environment variable:

```bash
# Development (default — set in manage.py)
DJANGO_SETTINGS_MODULE=config.settings.development

# Production (set in your systemd service / Docker ENV / Heroku config)
DJANGO_SETTINGS_MODULE=config.settings.production

# Testing (set automatically by pytest.ini)
DJANGO_SETTINGS_MODULE=config.settings.testing
```

### Adding a setting

1. If it belongs in **all** environments → add to `base.py`
2. If it's **dev-only** (e.g. a debug panel) → add to `development.py`
3. If it's **prod-only** (e.g. HSTS) → add to `production.py`
4. If it needs a **secret value** → read it from `.env` via `env("MY_VAR")`

```python
# base.py example
MY_SETTING = env("MY_SETTING", default="fallback_value")
MY_INT      = env.int("MY_INT", default=10)
MY_BOOL     = env.bool("MY_BOOL", default=False)
MY_LIST     = env.list("MY_LIST", default=[])
```

---

## Environment Variables

Copy `.env.example` → `.env`. The table below describes every variable.

| Variable | Required | Default | Description |
|---|---|---|---|
| `DJANGO_SECRET_KEY` | ✅ | — | Django secret key. Generate a new one per environment. |
| `DJANGO_DEBUG` | | `False` | Set `True` in development only. |
| `DJANGO_ALLOWED_HOSTS` | ✅ prod | `[]` | Comma-separated list of allowed hostnames. |
| `DATABASE_URL` | | `sqlite:///db.sqlite3` | Full DB URL. E.g. `postgres://user:pass@host/db` |
| `REDIS_URL` | | `redis://localhost:6379/1` | Redis URL for cache. |
| `CELERY_BROKER_URL` | | `redis://localhost:6379/0` | Celery broker (Redis or RabbitMQ). |
| `CELERY_RESULT_BACKEND` | | `redis://localhost:6379/0` | Where Celery stores task results. |
| `DEFAULT_FROM_EMAIL` | | `noreply@example.com` | From address for outgoing email. |
| `EMAIL_HOST` | ✅ prod | — | SMTP server hostname. |
| `EMAIL_PORT` | | `587` | SMTP port. |
| `EMAIL_USE_TLS` | | `True` | Use TLS for SMTP. |
| `EMAIL_HOST_USER` | ✅ prod | — | SMTP username. |
| `EMAIL_HOST_PASSWORD` | ✅ prod | — | SMTP password / API key. |
| `SITE_NAME` | | `MyProject` | Used in templates and email subjects. |
| `SITE_URL` | | `http://localhost:8000` | Full site URL for email links. |
| `SITE_TAGLINE` | | `""` | Used in `<meta description>`. |
| `DJANGO_TIMEZONE` | | `UTC` | Server timezone. E.g. `Europe/London`. |
| `DJANGO_ADMIN_URL` | | `admin/` | Admin path. Change in production. E.g. `x7km-admin/` |
| `CORS_ALLOWED_ORIGINS` | | `""` | Comma-separated origins for CORS. |

---

## Adding a New App

This is the most common task — here's the full workflow for adding a `blog` app.

### Step 1 — Scaffold the app

```bash
# Option A: Makefile shortcut (recommended)
make newapp name=blog

# Option B: Python script
python scripts/new_app.py blog
```

This creates `apps/blog/` with all files pre-wired:
```
apps/blog/
  __init__.py
  apps.py          ← AppConfig with signals connected
  models.py        ← commented example extending TimeStampedUUIDModel
  views.py         ← commented example CBVs
  urls.py          ← app_name = "blog" ready
  forms.py
  admin.py
  services.py      ← business logic goes here, not in views
  tasks.py         ← Celery tasks
  signals.py
  migrations/
  api/
    serializers.py
    views.py
    urls.py
  tests/
    test_models.py
    test_views.py
    test_api.py
```

### Step 2 — Register the app

In `config/settings/base.py`, add to `LOCAL_APPS`:

```python
LOCAL_APPS = [
    "apps.core",
    "apps.users",
    "apps.blog",   # ← add this
]
```

### Step 3 — Wire up URLs

In `config/urls.py`:

```python
urlpatterns = [
    # ... existing ...

    # Web routes
    path("blog/", include("apps.blog.urls", namespace="blog")),

    # API routes (inside the api/v1/ group)
    path("api/v1/", include([
        path("users/", include("apps.users.api.urls", namespace="users-api")),
        path("blog/",  include("apps.blog.api.urls",  namespace="blog-api")),  # ← add
    ])),
]
```

### Step 4 — Define your model and migrate

```python
# apps/blog/models.py
from apps.core.models import TimeStampedUUIDModel
from django.db import models
from django.conf import settings

class Post(TimeStampedUUIDModel):
    author  = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title   = models.CharField(max_length=200)
    content = models.TextField()
    published = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title
```

```bash
python manage.py makemigrations blog
python manage.py migrate
```

### Step 5 — Add to admin

```python
# apps/blog/admin.py
from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display  = ("title", "author", "published", "created_at")
    list_filter   = ("published",)
    search_fields = ("title", "author__email")
```

That's it. The app is fully wired.

---

## URL Routing

### Convention

| Pattern | Purpose | Example |
|---|---|---|
| `/` | Home (redirects to dashboard) | |
| `/<app>/` | Web routes for an app | `/blog/` |
| `/api/v1/<app>/` | REST API routes | `/api/v1/blog/` |
| `/<ADMIN_URL>/` | Django admin (randomised in prod) | `/admin/` |
| `/core/health/` | Health check for load balancers | |

### Namespacing

Every app's `urls.py` sets `app_name`:

```python
# apps/blog/urls.py
app_name = "blog"

urlpatterns = [
    path("",          views.PostListView.as_view(),   name="list"),
    path("<uuid:pk>/", views.PostDetailView.as_view(), name="detail"),
    path("new/",      views.PostCreateView.as_view(),  name="create"),
]
```

Then in templates:
```html
<a href="{% url 'blog:list' %}">All posts</a>
<a href="{% url 'blog:detail' pk=post.pk %}">Read more</a>
```

And in Python:
```python
from django.urls import reverse
reverse("blog:list")
reverse("blog:detail", kwargs={"pk": post.pk})
```

---

## Users App

The `apps/users` app ships with everything you'd want for a user system.

### Model fields

| Field | Type | Notes |
|---|---|---|
| `id` | UUID | Primary key — not guessable in URLs |
| `email` | EmailField | USERNAME_FIELD — unique |
| `first_name` / `last_name` | CharField | |
| `avatar` | ImageField | Uploaded to `media/avatars/<uuid>/` |
| `bio` | TextField | max 500 chars |
| `phone` | CharField | |
| `timezone` | CharField | Default `UTC` |
| `website` | URLField | |
| `is_email_verified` | BooleanField | Set after verification flow |
| `is_active` / `is_staff` | BooleanField | Standard Django flags |
| `created_at` / `updated_at` | DateTimeField | From `TimeStampedModel` |

### Web routes (all under `/users/`)

| URL | View | Name |
|---|---|---|
| `register/` | RegisterView | `users:register` |
| `login/` | CustomLoginView | `users:login` |
| `logout/` | CustomLogoutView | `users:logout` |
| `dashboard/` | DashboardView | `users:dashboard` |
| `profile/` | ProfileView (own) | `users:profile` |
| `profile/<uuid:pk>/` | ProfileView (other) | `users:profile-detail` |
| `profile/edit/` | ProfileUpdateView | `users:profile-edit` |
| `settings/` | AccountSettingsView | `users:settings` |
| `settings/password/` | CustomPasswordChangeView | `users:password-change` |
| `settings/delete/` | AccountDeleteView | `users:account-delete` |
| `password-reset/` | Password reset flow | `users:password_reset` |

### Customising registration

To add custom fields to registration, edit `apps/users/forms.py` (`RegisterForm`)
and `apps/users/views.py` (`RegisterView`). The form automatically handles
duplicate email checks and password confirmation.

---

## REST API

The API uses DRF Token Authentication.

### Auth flow

```bash
# Register
POST /api/v1/users/register/
{ "email": "alice@example.com", "first_name": "Alice",
  "last_name": "Smith", "password": "pass", "password2": "pass" }
# → { "token": "abc123", "user": { ... } }

# Login
POST /api/v1/users/login/
{ "username": "alice@example.com", "password": "pass" }
# → { "token": "abc123", "user": { ... } }

# Authenticated requests — add header:
Authorization: Token abc123

# Get own profile
GET /api/v1/users/me/

# Update own profile
PATCH /api/v1/users/me/
{ "first_name": "Alicia", "bio": "Hello!" }

# Change password
POST /api/v1/users/me/change-password/
{ "old_password": "pass", "new_password": "newpass", "new_password2": "newpass" }

# Logout (invalidates token)
POST /api/v1/users/logout/

# Public profile
GET /api/v1/users/<uuid>/
```

### Adding API endpoints to a new app

```python
# apps/blog/api/views.py
from rest_framework import generics, permissions
from apps.blog.models import Post
from .serializers import PostSerializer

class PostListAPIView(generics.ListCreateAPIView):
    queryset           = Post.objects.filter(published=True)
    serializer_class   = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
```

---

## Celery Tasks

### Writing a task

```python
# apps/blog/tasks.py
from celery import shared_task
import logging

logger = logging.getLogger(__name__)

@shared_task(bind=True, max_retries=3, default_retry_delay=60)
def notify_subscribers_task(self, post_id):
    try:
        from apps.blog.models import Post
        post = Post.objects.get(pk=post_id)
        # ... send emails ...
        logger.info("Notified subscribers for post %s", post_id)
    except Exception as exc:
        raise self.retry(exc=exc)
```

### Calling a task

```python
# Async (real Celery worker required)
notify_subscribers_task.delay(post.pk)

# With countdown (delay in seconds)
notify_subscribers_task.apply_async(args=[post.pk], countdown=30)

# Synchronous (in development — CELERY_TASK_ALWAYS_EAGER=True)
notify_subscribers_task(post.pk)
```

### Starting the worker

```bash
# In development — tasks run synchronously (no worker needed)
# CELERY_TASK_ALWAYS_EAGER=True is set in development.py

# In production
celery -A config.celery_app worker -l info

# Or via Docker Compose (included by default)
docker compose up celery
```

---

## Running Tests

```bash
# Run all tests
make test                   # or: pytest

# With coverage report
make test-cov               # generates htmlcov/index.html

# Run a specific test file
pytest apps/users/tests.py

# Run a specific test class
pytest apps/users/tests.py::TestRegisterAPI

# Run a specific test
pytest apps/users/tests.py::TestRegisterAPI::test_register_success

# Run only fast tests (skip slow-marked)
pytest -m "not slow"

# Run in parallel (faster on multi-core)
pytest -n auto
```

### Writing tests

```python
# apps/blog/tests/test_api.py
import pytest
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.fixture
def auth_client(db):
    user = User.objects.create_user(email="test@example.com", password="pass")
    client = APIClient()
    client.force_authenticate(user=user)
    return client

@pytest.mark.django_db
class TestPostAPI:
    def test_list_posts(self, auth_client):
        res = auth_client.get("/api/v1/blog/")
        assert res.status_code == status.HTTP_200_OK
```

---

## Docker

### Development

```bash
# Start everything
docker compose up

# Start only infrastructure (postgres + redis), run Django locally
docker compose up postgres redis

# Run one-off management commands
docker compose run --rm web python manage.py migrate
docker compose run --rm web python manage.py createsuperuser
docker compose run --rm web python manage.py shell_plus

# View logs
docker compose logs -f web
docker compose logs -f celery

# Stop everything
docker compose down

# Destroy volumes (full reset)
docker compose down -v
```

### Production Docker build

```bash
# Build the image
docker build -t myproject:latest .

# Run with production settings
docker run -d \
  --env-file .env \
  -e DJANGO_SETTINGS_MODULE=config.settings.production \
  -p 8000:8000 \
  myproject:latest
```

---

## Production Deployment

### Checklist

- [ ] Set `DJANGO_SECRET_KEY` to a new random value
- [ ] Set `DJANGO_DEBUG=False`
- [ ] Set `DJANGO_ALLOWED_HOSTS` to your domain(s)
- [ ] Set `DATABASE_URL` to PostgreSQL connection string
- [ ] Set `DJANGO_ADMIN_URL` to a secret path (e.g. `x7k2m9-admin/`)
- [ ] Configure `EMAIL_HOST` and credentials
- [ ] Set `SITE_URL` to your HTTPS domain
- [ ] Set `CORS_ALLOWED_ORIGINS` to your frontend domain(s)
- [ ] Run `python manage.py migrate`
- [ ] Run `python manage.py collectstatic --noinput`
- [ ] Set `DJANGO_SETTINGS_MODULE=config.settings.production` in your process manager
- [ ] Point Nginx at Gunicorn (see `docs/nginx.conf`)
- [ ] Set up SSL with Let's Encrypt: `certbot --nginx -d yourdomain.com`

### Gunicorn

```bash
gunicorn config.wsgi:application \
    --workers 4 \
    --worker-class gthread \
    --threads 2 \
    --bind 0.0.0.0:8000 \
    --access-logfile - \
    --error-logfile -
```

**Worker count rule of thumb:** `(2 × CPU cores) + 1`

### Platform-specific guides

- **Heroku**: Set Config Vars in dashboard. Add `Procfile`:
  ```
  web: gunicorn config.wsgi:application
  worker: celery -A config.celery_app worker -l info
  ```
- **Railway / Render**: Set `DJANGO_SETTINGS_MODULE=config.settings.production` in env vars. Build command: `pip install -r requirements/production.txt && python manage.py collectstatic --noinput && python manage.py migrate`. Start command: `gunicorn config.wsgi:application`.
- **VPS (Ubuntu)**: Use `docs/nginx.conf` + systemd service + certbot.

---

## Code Quality

```bash
# Lint (check for issues)
make lint           # ruff check .

# Format (auto-fix style)
make format         # ruff format . && ruff check --fix .

# Run lint + tests together
make check

# Install pre-commit hooks (runs on every git commit)
pre-commit install

# Run pre-commit manually on all files
pre-commit run --all-files
```

### pre-commit hooks included

- `trailing-whitespace` — remove trailing spaces
- `end-of-file-fixer` — ensure files end with newline
- `check-yaml` / `check-json` — validate config files
- `detect-private-key` — prevent accidental key commits
- `ruff` — lint + auto-fix
- `ruff-format` — consistent formatting
- `detect-secrets` — prevent committing secrets

---

## License

MIT — use freely for personal and commercial projects.
