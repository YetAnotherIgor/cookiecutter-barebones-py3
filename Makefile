SHELL := /bin/bash

.PHONY: all clean clean_all test example-project

all: clean test

clean:
	-rm -r example-project

clean_all: clean
	-rm -r .virtualenv

.virtualenv/bin/activate:
	virtualenv -p python3 .virtualenv
	.virtualenv/bin/pip3 install cookiecutter tox

example-project: .virtualenv/bin/activate
	source .virtualenv/bin/activate && cookiecutter . --no-input

test: example-project .virtualenv/bin/activate
	source .virtualenv/bin/activate && cd ./example-project && make
