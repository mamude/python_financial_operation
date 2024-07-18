SHELL := /bin/bash

create-env:
	@python -m venv .venv && pip install --upgrade pip && pip install poetry

activate-env:
	@source .venv/bin/activate

install:
	@poetry install

run:
	@flask --app src/app run --debug

docker-run:
	@docker compose up -d

test:
	@coverage run -m pytest

coverage:
	@coverage report
	@coverage html

migrate-up:
	@alembic upgrade head

lint:
	@pylint src/app/*

format:
	@black src/app/*