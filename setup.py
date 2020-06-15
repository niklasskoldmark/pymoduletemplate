# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open("README.rst") as f:
    readme = f.read()

with open("LICENSE") as f:
    license = f.read()

setup(
    name="pymoduletemplate",
    version="0.1.0",
    description="pymoduletemplate",
    long_description=readme,
    author="Niklas Skoldmark",
    author_email="niklas.skoldmark@gmail.com",
    url="https://github.com/niklasskoldmark/pymoduletemplate",
    license=license,
    packages=find_packages(exclude=("tests", "docs")),
)
