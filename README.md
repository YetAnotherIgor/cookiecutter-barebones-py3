# cookiecutter-barebones-py3

Barebones [cookiecutter template](https://github.com/audreyr/cookiecutter) for a Python 3.x project.

Tailored to be the bare minimum for a personal Python 3.x project.

## Caveats

* Still a work in progress
* Not making release tags etc., `master` is the latest semi-working cut.
* Biased towards adhoc personal projects that aren't going on PyPI any time soon.
* If you want more than this please refer to the plethora of much more mature and
  fully featured Python project cookiecutters out there.

## Influences

Based off these project structures:

* [audreyr's cookiecutter-pypackage](https://github.com/audreyr/cookiecutter-pypackage)
* [PyPA Sample Project](https://github.com/pypa/sampleproject)

## Prerequisites

* One of these Python interpreters
  * Python 3.4
  * Python 3.5
  * Python 3.6
* These Python packages
  * ``virtualenv`` 
* Make

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

