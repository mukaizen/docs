# ──────────────────────────────────────────────────────────────────────────────
#  Makefile — common development commands
#  Usage: make <target>
# ──────────────────────────────────────────────────────────────────────────────

.PHONY: help install dev test lint format migrate superuser shell \
        celery worker beat docker-up docker-down clean

# Default target
help:
	@echo ""
	@echo "  Django Boilerplate — available commands"
	@echo ""
	@echo "  Setup"
	@echo "    make install       Install all dev dependencies"
	@echo "    make env           Copy .env.example → .env"
	@echo ""
	@echo "  Development"
	@echo "    make dev           Run development server"
	@echo "    make migrate       Run makemigrations + migrate"
	@echo "    make superuser     Create a superuser"
	@echo "    make shell         Open Django shell_plus"
	@echo "    make worker        Start Celery worker"
	@echo "    make beat          Start Celery beat"
	@echo ""
	@echo "  Quality"
	@echo "    make test          Run test suite"
	@echo "    make test-cov      Run tests with coverage report"
	@echo "    make lint          Run ruff linter"
	@echo "    make format        Run ruff formatter"
	@echo "    make check         lint + test"
	@echo ""
	@echo "  Docker"
	@echo "    make docker-up     Start full stack (web + postgres + redis + celery)"
	@echo "    make docker-down   Stop all containers"
	@echo "    make docker-build  Rebuild images"
	@echo ""
	@echo "  Utility"
	@echo "    make clean         Remove .pyc, __pycache__, coverage files"
	@echo "    make static        Collect static files"
	@echo "    make newapp        Scaffold a new app: make newapp name=blog"
	@echo ""

# ── Setup ─────────────────────────────────────────────────────────────────────

env:
	@test -f .env || (cp .env.example .env && echo "✓ .env created — fill in your values")

install: env
	pip install --upgrade pip
	pip install -r requirements/development.txt
	pre-commit install
	@echo "✓ Dependencies installed"

# ── Development ───────────────────────────────────────────────────────────────

dev:
	DJANGO_SETTINGS_MODULE=config.settings.development \
	python manage.py runserver 0.0.0.0:8000

migrate:
	python manage.py makemigrations
	python manage.py migrate

superuser:
	python manage.py createsuperuser

shell:
	python manage.py shell_plus --ipython

worker:
	celery -A config.celery_app worker -l info --concurrency 2

beat:
	celery -A config.celery_app beat -l info \
	    --scheduler django_celery_beat.schedulers:DatabaseScheduler

# ── Quality ───────────────────────────────────────────────────────────────────

test:
	pytest

test-cov:
	pytest --cov=apps --cov-report=html --cov-report=term-missing
	@echo "✓ Coverage report: htmlcov/index.html"

lint:
	ruff check .

format:
	ruff format .
	ruff check --fix .

check: lint test

# ── Docker ────────────────────────────────────────────────────────────────────

docker-up:
	docker compose up

docker-down:
	docker compose down

docker-build:
	docker compose build

docker-migrate:
	docker compose run --rm web python manage.py migrate

docker-superuser:
	docker compose run --rm web python manage.py createsuperuser

# ── Utility ───────────────────────────────────────────────────────────────────

static:
	python manage.py collectstatic --noinput

clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null; true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null; true
	rm -rf htmlcov .coverage coverage.xml .pytest_cache
	@echo "✓ Cleaned"

# ── New app scaffold ──────────────────────────────────────────────────────────
# Usage: make newapp name=blog

newapp:
	@test -n "$(name)" || (echo "Usage: make newapp name=<appname>" && exit 1)
	mkdir -p apps/$(name)/api apps/$(name)/migrations apps/$(name)/tests
	python manage.py startapp $(name) apps/$(name)
	touch apps/$(name)/api/__init__.py
	touch apps/$(name)/api/serializers.py
	touch apps/$(name)/api/views.py
	touch apps/$(name)/api/urls.py
	touch apps/$(name)/urls.py
	touch apps/$(name)/services.py
	touch apps/$(name)/tasks.py
	touch apps/$(name)/tests/__init__.py
	touch apps/$(name)/tests/test_models.py
	touch apps/$(name)/tests/test_views.py
	touch apps/$(name)/tests/test_api.py
	@echo ""
	@echo "✓ App '$(name)' scaffolded at apps/$(name)/"
	@echo ""
	@echo "  Next steps:"
	@echo "  1. Add \"apps.$(name)\" to LOCAL_APPS in config/settings/base.py"
	@echo "  2. Add web routes in config/urls.py:"
	@echo "       path(\"$(name)/\", include(\"apps.$(name).urls\", namespace=\"$(name)\")),"
	@echo "  3. Add API routes in config/urls.py:"
	@echo "       path(\"$(name)/\", include(\"apps.$(name).api.urls\", namespace=\"$(name)-api\")),"
	@echo "  4. Run: make migrate"
	@echo ""
