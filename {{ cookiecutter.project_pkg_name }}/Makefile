SHELL := /bin/bash
export TOXENV = $(shell python3 -c "import sys; print(\"py{}{}\".format(sys.version_info.major, sys.version_info.minor))")

.PHONY: all build clean dist lint lint_tests test

all: clean lint lint_tests test build dist

clean:
	-rm -rv build/ dist/ .eggs/ *.egg-info/
	-find . -name "*.pyc" -delete
	-find . -name "*.pyo" -delete
	-find . -name "__pycache__" -delete
	-find . -name '*.egg' -delete

clean_all: clean
	-rm -rv .tox
	-rm -f .coverage htmlcov/

.tox/$(TOXENV)/bin/pylint:
	tox --notest

lint: .tox/$(TOXENV)/bin/pylint
	.tox/$(TOXENV)/bin/pylint {{ cookiecutter.project_module_name }}

lint_tests: .tox/$(TOXENV)/bin/pylint
	.tox/$(TOXENV)/bin/pylint --errors-only tests

test:
	tox -- test

build:
	tox -- build

dist: clean
	tox -- sdist
	tox -- bdist_wheel
	ls -l dist/

