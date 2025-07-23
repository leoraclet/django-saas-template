PYTHON = uv run
MANAGE_PY = $(PYTHON) manage.py

.PHONY:
honcho:
	$(PYTHON) -m honcho start -e DATABASE=sqlite

.PHONY:
migrations:
	cd server && $(MANAGE_PY) makemigrations

.PHONY:
migrate:
	cd server && $(MANAGE_PY) migrate

.PHONY:
run:
	cd server && $(MANAGE_PY) runserver

.PHONY:
shell:
	cd server && $(MANAGE_PY) shell

.PHONY:
frontend:
	cd frontend && npm run dev

.PHONY:
build:
	docker compose -f docker-compose.test.yml build --no-cache

.PHONY:
up:
	docker compose -f docker-compose.test.yml up -d

.PHONY:
down:
	docker compose -f docker-compose.test.yml down

.PHONY:
logs:
	docker compose -f docker-compose.test.yml logs -f
