#!/usr/bin/env python
"""
Flask-RequestUID
=============
A flask extension to add a unique identifier to the request for tracing and logging.

See README.md for more information.
"""
import re

from setuptools import setup

with open("src/flask_request_uid/__init__.py", encoding="utf8") as fp:
    version = re.search(r'__version__ = "(.*?)"', fp.read()).group(1)

extra_requires = {
    "dev": ['pre-commit'],
    "docs": ["safety", "sphinx"],
    "lint": ['flake8', 'pylint', 'yamllint', 'yapf'],
    "test": ['coverage', 'pytest', 'pytest-cov', 'safety'],
}

setup(
    version=version,
    install_requires=[''],
    extras_require=extra_requires,
    zip_safe=False,
    platforms="any",
)
