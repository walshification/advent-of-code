PIPENV_RUN := pipenv run
AUTOFLAKE := $(PIPENV_RUN) autoflake
BLACK := $(PIPENV_RUN) black
IPYTHON := $(PIPENV_RUN) ipython
ISORT := $(PIPENV_RUN) isort
MYPY := $(PIPENV_RUN) mypy
PYTEST := $(PIPENV_RUN) pytest

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
