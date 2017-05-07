#
# Taken in large part from https://raw.githubusercontent.com/audreyr/cookiecutter-pypackage/master/%7B%7Bcookiecutter.project_slug%7D%7D/Makefile
#

SHELL := /bin/bash
export TOXENV = $(shell python3 -c "import sys; print(\"py{}{}\".format(sys.version_info.major, sys.version_info.minor))")

## setup default target
all: clean lint test dist

## remove all build, test, coverage and Python artifacts
clean: clean_build clean_pyc clean_test

## remote all transient artifacts
clean_all: clean clean_tox

## remove .tox etc.
clean_tox:
	-rm -rfv .tox

## remove build artifacts
clean_build:
	-rm -frv build/ dist/ .eggs/
	-find . -name '*.egg-info' -exec rm -fr {} +
	-find . -name '*.egg' -exec rm -f {} +

## remove Python file artifacts
clean_pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

## remove test and coverage artifacts
clean_test:
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/

## lint with pylint
lint:
	tox --notest
	.tox/$(TOXENV)/bin/pylint --rcfile pylintrc {{ cookiecutter.project_module_name }}

## run tests
test:
	tox -- test

## build source and wheel distribution packages
dist: clean
	tox -- sdist
	tox -- bdist_wheel
	ls -l dist/

