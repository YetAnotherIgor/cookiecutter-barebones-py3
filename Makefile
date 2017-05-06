SHELL := /bin/bash

TOXENV = $(shell python3 -c "import sys; print(\"py{}{}\".format(sys.version_info.major, sys.version_info.minor))")

.PHONY: all clean clean_all test

all: clean test

clean:
	-rm -r example-project

clean_all: clean
	-rm -r .tox .virtualenv

.virtualenv/bin/activate:
	virtualenv -p python3 .virtualenv
	.virtualenv/bin/pip3 install tox

example-project: .virtualenv/bin/activate
	.virtualenv/bin/tox

test: example-project .virtualenv/bin/activate
	source .virtualenv/bin/activate && cd ./example-project && make
