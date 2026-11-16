# Contributing to {{ cookiecutter.package_distribution_name }}

## Set up for development

Activate a Python 3.11+ virtual environment in the project directory.

```sh
python -m pip install -e .
```

## Run the tests

```sh
python -c "from {{ cookiecutter.package_import_name }} import greet; print(greet('Hee'))"
```

Expected output: `Hello, Hee!`

## Send a change

1. Switch to `main` and create a branch from it.
2. Make and commit your change on that branch, then push the branch.
3. Open a pull request from your branch into `main`.
