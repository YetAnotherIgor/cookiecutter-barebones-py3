# cookiecutter-barebones-py3

Barebones [cookiecutter template](https://github.com/audreyr/cookiecutter) for a Python 3.x project.

Tailored to be the bare minimum for a personal Python 3.x project.

## Caveats

* Intended for adhoc personal projects that aren't going on PyPI any time soon.
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

Point the ``cookiecutter`` tool at the git URL for this repository and let it default
to using the ``master`` branch.

## Development

### Testing

A crude smoke testing recipe is included in the repository.
 
Run it using the included Makefile, and it will do the following:

* Makefile runs tox with the "outer" config (<repo-root>/tox.ini)
* Inside the "outer" tox config, ``cookiecutter`` is run to emit an instance of the templated project.
* The Makefile logic then runs the "inner" tox config emitted as part of the template project.

Kick it all off by running this:

```
make
```
### Release management 

* Branching is as follows:
    * The ``master`` branch is the latest "production" cut
    * The ``develop`` branch is the latest in-progress draft
* Tags are made for each "release" of the template
    * The ``cookiecutter`` tool itself has no concept of versions of a template other than
      the URL it is given.  When given a URL/path to a valid Git repo, it defaults to 
      using the ``master`` branch (although you can override this at the cli etc.).
    * So these tags are more of a breadcrumb trail for the maintainer than something the
      ``cookiecutter`` tool would use directly.
    * A date-based versioning scheme is used for the tag names.
