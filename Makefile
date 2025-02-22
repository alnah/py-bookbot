ENV=env
PIP=$(ENV)/bin/pip
RUFF=$(ENV)/bin/ruff
PYRIGHT=$(ENV)/bin/pyright

.PHONY: default env install-dev check fmt lintfix lsp

default: check

check: env lsp fmt

env:
	$(info 🌍 ACTIVATING ENVIRONMENT...)
	@if [ ! -d "$(ENV)" ]; then python -m venv $(ENV); fi

install-dev: env
	$(info 📥 DOWNLOADING DEPENDENCIES...)
	$(PIP) install -r requirements_dev.txt

lsp: env
	$(info 🛠️ CHECKING STATIC TYPES...)
	$(PYRIGHT)

lintfix: env
	$(info 🔍 RUNNING LINT TOOLS...)
	$(RUFF) check --select I --fix

fmt: env
	$(info ✨ CHECKING CODE FORMATTING...)
	$(RUFF) format
