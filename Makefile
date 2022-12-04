VENV_BIN := .venv/bin
AUTOFLAKE := $(VENV_BIN)/autoflake
BLACK := $(VENV_BIN)/black
IPYTHON := $(VENV_BIN)/ipython
ISORT := $(VENV_BIN)/isort
MYPY := $(VENV_BIN)/mypy
PYTEST := $(VENV_BIN)/pytest

.PHONY: test lint pytest install clean shell

test: lint pytest

fmt:
	$(AUTOFLAKE) .
	$(ISORT) .
	$(BLACK) .

lint:
	$(AUTOFLAKE) --check .
	# pipenv run isort --check-only .
	$(BLACK) --check .
	$(MYPY) .

pytest:
	$(PYTEST)

shell:
	$(IPYTHON)

install:
	pyenv install -s
	pip install --upgrade pip
	pip install pipenv
	pipenv install

clean:
	pipenv --rm
