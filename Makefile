#Makefile

install:
	poetry install

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