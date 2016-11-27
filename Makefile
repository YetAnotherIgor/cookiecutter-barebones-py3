SHELL := /bin/bash

.PHONY: all clean clean_all test

all: clean test

clean:
	-rm -r example-project	

clean_all: clean
	-rm -r .tox .virtualenv

.virtualenv/bin/activate:
	virtualenv -p python3.5 .virtualenv
	.virtualenv/bin/pip3 install tox

example-project: .virtualenv/bin/activate
	.virtualenv/bin/tox

test: example-project .virtualenv/bin/activate
	cd ./example-project && ../.virtualenv/bin/tox

