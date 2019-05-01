
# XNATUM

![PyPI](https://img.shields.io/pypi/v/xnatum.svg) ![PyPI - Downloads](https://img.shields.io/pypi/dm/xnatum.svg) ![PyPI - Python Version](https://img.shields.io/pypi/pyversions/xnatum.svg) ![PyPI - Wheel](https://img.shields.io/pypi/wheel/xnatum.svg) ![PyPI - Implementation](https://img.shields.io/pypi/implementation/xnatum.svg) 

XNATUM is a Python client that exposes in a simple way XNAT objects and functions. The aim is to make a simple Python package to everyone to use on top of Xnatpy. This reduces the need for the user to know the details of the REST API.

## Getting started

To install just use the setup.py normally:

```python setup.py install```

or install directly via pip:

```pip install xnatum```

## Useful development commands

To compile it locally:

```python setup.py sdist bdist_wheel```

To install a local version:

```pip install ./dist/<archive> --upgrade```

To upload it to Pypi:

```python -m twine upload dist/*```

## Examples

You can find some code examples on how to use this package on the **examples** folder.

## Documentation

The official documentation is avaiable at xnatum.readthedocs.org.

## Workflow to contribute

To contribute to XNATUM, first create an Github account. Once this is done, fork the XNATUM repository to have you own repository, clone it using 'git clone'. Make your changes in your clone, push them to your forked repo, test them and when you are happy with them, send a pull request to the main repository.

## Status

This package is currently been developed part of my MSc. thesis.