#!/usr/bin/env python

from setuptools import setup, find_packages
import rinpy

setup(
    name="rinpy",
    version=rinpy.__version__,
    description="Python BDD Test Framework like mocha",
    url="https://github.com/float1251/rinpy",
    author="takahiro iwatani",
    author_email="taka.05022002@gmail.com",
    packages=find_packages(),
    test_suite="tests",
)
