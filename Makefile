.PHONY: test lint pytest install clean shell

test: lint pytest

lint:
	pipenv run black . --check
	pipenv run mypy .

pytest:
	# pipenv run pytest --cov-report term --cov-config=setup.cfg
	pipenv run pytest \
		--cov-config=setup.cfg \
		--cov=aoc_2015 \
		--cov-report html \
		--cov-report term-missing

shell:
	pipenv run ipython

install:
	pyenv install -s
	pip install --upgrade pip
	pip install pipenv
	pipenv install

clean:
	pipenv --rm
