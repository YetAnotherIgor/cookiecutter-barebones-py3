# cookiecutter-barebones-py35

Barebones [cookiecutter template](https://github.com/audreyr/cookiecutter) for a Python 3.5 project.

Tailored to be the bare minimum for a personal Python 3.5 project.

## Influences

Based off these project structures:

* [PyPA Sample Project](https://github.com/pypa/sampleproject)
* [audreyr's cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage)

## Prerequisites

* Python 3.5
* Make
* ``tox`` and ``virtualenv`` Python packages

## Usage

### Testing the template being generated

Run the included Makefile and tox to do the following:

* Makefile runs tox with the "outer" config (<repo-root>/tox.ini)
* Inside the "outer" tox config, ``cookiecutter`` is run to emit an instance of the templated project.
* The Makefile logic then runs the "inner" tox config emitted as part of the template project.

Kick it all off by running this:

```
make
```

The Makefile has several targets for slices of functionality to test.

