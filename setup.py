#!/usr/bin/env python
# encoding: utf-8


"""Canbus Explorer, graphical canbus activity monitoring by Craig J Perry"""

from setuptools import setup, find_packages


__version__ = "0.1.1"

README = open("README.rst").read()
REQUIREMENTS = open("dev-requirements.txt").readlines()


setup(
    name="canbus_explorer",
    version=__version__,
    author="Craig J Perry",
    author_email="craigp84@gmail.com",
    description=__doc__,
    long_description=README,
    packages=find_packages("src", exclude=['tests']),
    package_dir={"": "src"},
    install_requires=REQUIREMENTS,
    zip_safe=False,
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "canbus_explorer = canbus_explorer.runner:main",
        ]
    }
)

