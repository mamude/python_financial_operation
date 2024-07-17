SHELL := /bin/bash

create-env:
	@python -m venv .venv && pip install --upgrade pip && pip install poetry

activate-env:
	. .venv/bin/activate

install:
	@poetry install

run:
	@flask --app src/app run --debug

docker-run:
	@docker compose up -d

test:
	@coverage run -m pytest

migrate-up:
	@alembic upgrade head