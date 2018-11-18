SHELL := /bin/bash

.PHONY: all clean clean_all generate smoke_test virtualenv

all: clean smoke_test

clean:
	-rm -r example-project/

clean_all: clean
	-rm -r .venv/
	-rm -r .test_venv/

.venv/bin/cookiecutter:
	virtualenv -p python3 .venv
	.venv/bin/pip install cookiecutter tox

virtualenv: .venv/bin/cookiecutter

generate: .venv/bin/cookiecutter
	@echo "*******************************************************************************" 
	@echo
	@echo "Use the cookiecutter tool to generate a project from this template"
	@echo
	@echo "*******************************************************************************" 
	
	.venv/bin/cookiecutter .

smoke_test:.venv/bin/cookiecutter
	@echo "*******************************************************************************"
	@echo
	@echo "Smoke test this template"
	@echo
	@echo "*******************************************************************************" 
	
	.venv/bin/cookiecutter . --no-input --overwrite-if-exists
	cd ./example-project && make
	-rm -r .test_venv/
	virtualenv -p python3 .test_venv
	.test_venv/bin/pip install -r ./example-project/requirements.txt
	.test_venv/bin/pip install ./example-project/dist/example_project-0.1.0-py3-none-any.whl

