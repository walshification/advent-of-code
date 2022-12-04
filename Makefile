.PHONY: test lint pytest install clean shell

test: lint pytest

fmt:
	pipenv run autoflake .
	pipenv run isort .
	pipenv run black .

lint:
	pipenv run autoflake --check .
	pipenv run isort --check-only .
	pipenv run black --check .
	pipenv run mypy .

pytest:
	pipenv run pytest

shell:
	pipenv run ipython

install:
	pyenv install -s
	pip install --upgrade pip
	pip install pipenv
	pipenv install

clean:
	pipenv --rm
