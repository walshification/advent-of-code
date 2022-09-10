.PHONY: test lint pytest install clean

test: lint pytest

lint:
	pipenv run black . --check
	pipenv run mypy .

pytest:
	pipenv run pytest

install:
	pyenv install -s
	pip install --upgrade pip
	pip install pipenv
	pipenv install

clean:
	pipenv --rm
