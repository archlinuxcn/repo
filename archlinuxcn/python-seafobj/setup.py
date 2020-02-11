#!/usr/bin/env python2

from setuptools import find_packages, setup

setup(
    name = "seafobj",
    version = "7.1.1",
    author = "Seafile Ltd.",
    author_email = "info@seafile.com",
    description = ("Python library for accessing seafile data model"),
    license = "Apache2",
    url = "https://github.com/haiwen/seafobj",
    packages = find_packages(exclude=["test.*", "test"])
)
