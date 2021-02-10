#!/usr/bin/env python

"""
Install menu package. To install locally use:
    'pip install -e .'
"""

from setuptools import setup

setup(
    name="menu",
    version="0.0.1",
    author="Catherine Lan",
    author_email="yl4289@columbia.edu",
    license="GPLv3",
    description="A package for deciding what to eat",
    classifiers=["Programming Language :: Python :: 3"],
    entry_points={
        # "console_scripts": ["module = package/directory.__main__:main"]
        "console_scripts": ["foodmenu = test.__main__:main"]
    },
)