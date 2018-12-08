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

.PHONY: all build check check_tests clean clean_all docs dist test

all: clean check check_tests test build docs dist


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
	@echo "Making sure .pytest directory exists"
	-mkdir .pytest
	touch .pytest/.breadcrumb

.tox/$(TOXENV)/bin/pylint:
	@echo "Making sure tox has created a working directory"
	tox --notest

check: .tox/$(TOXENV)/bin/pylint
	@echo "********************************************************************************"
	@echo
	@echo "Run static checks on source code"
	@echo
	@echo "********************************************************************************"

	@echo
	@echo "Run pylint on source code"
	@echo
	.tox/$(TOXENV)/bin/pylint {{ cookiecutter.project_module_name }}

	@echo
	@echo "Run mypy on source code"
	@echo
	.tox/$(TOXENV)/bin/mypy {{ cookiecutter.project_module_name }}

check_tests: .tox/$(TOXENV)/bin/pylint
	@echo "********************************************************************************"
	@echo
	@echo "Run static checks on test code"
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
