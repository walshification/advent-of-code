.PHONY: test lint pytest install clean shell

test: lint pytest

lint:
	pipenv run black . --check
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
