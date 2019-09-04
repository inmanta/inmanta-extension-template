# {{ cookiecutter.project_name }}
{{ cookiecutter.project_description }}

## Prerequisites

The following commands install all the packages required to run the
extension and its tests. 

```bash
$ pip install -r requirements.txt
$ make build-pytest-inmanta-extensions
```

## Format code

The following command formats the code using the black and the isort
code formatter. 

```bash
$ make format
```

## Run tests

Tests can be run using make or using tox. In contrast to make, tox
creates its own Python virtualenv. This way tox can run the same test
suite for different versions of the Python interpreter.

### Using make:

```bash
$ make pep8  # Run pep8 style checks
$ make tests # Run unit tests
$ make mypy  # Run mypy type checks
```

### Using tox:

```bash
$ tox -e pep8  # Run pep8 style checks
$ tox -e py36  # Run unit tests with a python3.6 interpreter
$ tox -e py37  # Run unit tests with a python3.7 interpreter
$ tox -e mypy  # Run mypy type checks
```

Run multiple environments:

```bash
$ tox # Run the pep8, py36 and mypy in sequence
```

## Install package

Install all the packages in the requirements.txt file and install the
Inmanta extension in editable mode. This way changes in the source code
will be reflected in the installed package as well. 

```bash
$ make install
```