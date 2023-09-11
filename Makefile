#Makefile

install:
	poetry install

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=difference_calculator --cov-report xml

gendiff: # run gendiff
	poetry run gendiff

build: # build project
	poetry build

publish: # publish without PyPI
	poetry publish --dry-run

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl

lint: # run_linter
	poetry run flake8 difference_calculator
	
full: build publish package-install

selfcheck:
	poetry check

check: selfcheck test lint