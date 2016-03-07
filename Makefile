SHELL := /bin/bash

.PHONY: all clean test

all: clean test_all

clean:
	@echo Clean
	@if [[ -e ./tox ]]; then rm -r ./tox;  fi;
	@if [[ -e ./example-project ]]; then rm -r ./example-project;  fi;

example-project:
	@echo Running tox to generate project from template under test	
	tox

test_default_envs: example-project
	@echo Test the default tox environments in the template under test 	
	cd ./example-project && tox

test_lint: example-project
	@echo Test the linting in the template under test 	
	cd ./example-project && tox -e py35_lint

test_build_wheel: example-project
	@echo Test building a wheel using the template under test 
	cd ./example-project && tox -e py35_wheel

test_build_docs: example-project
	@echo Test building docs using the template under test 
	cd ./example-project && tox -e py35_docs

test_all: test_default_envs test_lint test_build_wheel test_build_docs
	@echo Test all

