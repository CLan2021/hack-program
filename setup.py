#!/usr/bin/env python

"""
Install menu package. To install locally use:
    'pip install -e .'
"""

from setuptools import setup

setup(
    name="menu",
    version="0.0.1",
    packages=[],
    entry_points={
        "console_scripts": ["test = menu.__main__:main"]
    },
)