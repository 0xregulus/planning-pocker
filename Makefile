VENV := venv
BIN := $(VENV)/bin
PYTHON := $(BIN)/python
SHELL := /bin/bash

include .env

.PHONY: help
help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: venv
venv: ## Make a new virtual environment
	python3 -m venv $(VENV) && source $(BIN)/activate

.PHONY: install
install: venv ## Make venv and install requirements
	$(BIN)/pip install --upgrade -r requirements.txt

migrate: ## Make and run migrations
	$(PYTHON) manage.py makemigrations
	$(PYTHON) manage.py migrate

.PHONY: test
test: ## Run tests
	coverage run --source='.' --omit="*/venv/*" manage.py test --settings=planningpocker.settings.testing
	coverage report -m

.PHONY: run
run: ## Run the Django server
	$(PYTHON) manage.py runserver

start: install migrate run ## Install requirements, apply migrations, then start development server

.PHONY: install_front
install_front:
	bash -c "cd frontend && npm install"

.PHONY: run_front
run_front: install_front
	bash -c "cd frontend && npm start"

.PHONY: docker
up: ## Docker build and up
	docker-compose up -d --build

down: ## Docker down
	docker-compose down
