MANAGE_PY := "uv run manage.py"

honcho:
	uv run honcho start -e DATABASE=sqlite

migrations:
	cd server && {{MANAGE_PY}} makemigrations

migrate:
	cd server && {{MANAGE_PY}} migrate

run:
	cd server && {{MANAGE_PY}} runserver

shell:
	cd server && {{MANAGE_PY}} shell

frontend:
	cd frontend && npm run dev

build:
	docker compose -f docker-compose.test.yml build --no-cache

up:
	docker compose -f docker-compose.test.yml up -d

down:
	docker compose -f docker-compose.test.yml down
