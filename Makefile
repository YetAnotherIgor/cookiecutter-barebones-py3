SHELL := /bin/bash

.PHONY: all build clean clean_all test virtualenv

all: clean build test

clean:
	-rm -r example-project/

clean_all: clean
	-rm -r .venv/
	-rm -r .testvenv/

.venv/bin/activate:
	virtualenv -p python3 .venv
	.venv/bin/pip install cookiecutter tox

virtualenv: .venv/bin/activate

build: virtualenv
	.venv/bin/cookiecutter . --no-input --overwrite-if-exists

test:
	cd ./example-project && make
	-rm .testvenv/
	virtualenv -p python3 .testvenv
	.testvenv/bin/pip install -r ./example-project/requirements.txt
	.testvenv/bin/pip install ./example-project/dist/example_project-0.1.0-py3-none-any.whl

