#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
from setuptools import setup, find_packages
 
setup(
    name='PSTymer',
    version="0.0.1",
    packages=find_packages(),
    author="Znax & reco team",
    description="Monitor time for Python code",
    long_description=open('README.rst').read(),
    include_package_data=True,
    url='https://github.com/Znax/python-simple-timer',
    license="WTFPL"
)