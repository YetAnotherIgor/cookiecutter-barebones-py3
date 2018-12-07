##
# Makefile for common dev chores
#
# Caveats:
# * Assumes you are on a Linux/MacOS like operating system.  Is NOT compatible with Windows.
# * Assumes you already have Python etc. setup
#
##

SHELL := /bin/bash

export TOXENV = $(shell python3 -c "import sys; print(\"py{}{}\".format(sys.version_info.major, sys.version_info.minor))")

.PHONY: all build clean clean_all docs dist lint lint_tests test

all: clean lint lint_tests test build docs dist


clean:
	@echo "********************************************************************************"
	@echo
	@echo "Clean"
	@echo
	@echo "********************************************************************************"

	-rm -rv build/ dist/ .eggs/ *.egg-info/
	-find . -name "*.pyc" -delete
	-find . -name "*.pyo" -delete
	-find . -name "__pycache__" -delete
	-find . -name '*.egg' -delete

clean_all: clean
	@echo "********************************************************************************"
	@echo
	@echo "Clean all"
	@echo
	@echo "********************************************************************************"

	-rm -r pytest/
	-rm -r .tox/ 
	-rm -f .coverage
	-rm pytest.log

.pytest/.breadcrumb:
	-mkdir .pytest
	touch .pytest/.breadcrumb

.tox/$(TOXENV)/bin/pylint:
	tox --notest

lint: .tox/$(TOXENV)/bin/pylint
	@echo "********************************************************************************"
	@echo
	@echo "Lint source code"
	@echo
	@echo "********************************************************************************"

	.tox/$(TOXENV)/bin/pylint {{ cookiecutter.project_module_name }}

lint_tests: .tox/$(TOXENV)/bin/pylint
	@echo "********************************************************************************"
	@echo
	@echo "Lint test code"
	@echo
	@echo "********************************************************************************"

	.tox/$(TOXENV)/bin/pylint --errors-only tests

test: .pytest/.breadcrumb
	@echo "********************************************************************************"
	@echo
	@echo "Run tests"
	@echo
	@echo "********************************************************************************"

	@echo
	@echo "Running the unit and integration tests via pytest"
	@echo

	tox -- test

build:
	@echo "********************************************************************************"
	@echo
	@echo "Build"
	@echo
	@echo "********************************************************************************"

	tox -- build

docs:
	@echo "********************************************************************************"
	@echo
	@echo "Build Sphinx Docs"
	@echo
	@echo "********************************************************************************"
	tox -- sphinx_build


dist: clean
	@echo "********************************************************************************"
	@echo
	@echo "Prepare a distribution of the project"
	@echo
	@echo "********************************************************************************"

	tox -- sdist
	tox -- bdist_wheel
	ls -l dist/
