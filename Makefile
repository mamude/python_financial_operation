SHELL := /bin/bash

create-env:
	@python -m venv .venv && pip install --upgrade pip && pip install poetry

activate-env:
	. .venv/bin/activate

install:
	@poetry install

run:
	@flask --app src/app run --debug

check-routes:
	@quart --env-file .env --app src.api routes

docker-run:
	@docker compose up -d

test:
	@coverage run -m pytest

migrate-up:
	@alembic upgrade head