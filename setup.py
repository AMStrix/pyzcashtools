#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(name='bitcoin',
      version='0.1.0',
      description='Python Zcash Tools',
      author='Brad Miller',
      author_email='vbuterin@gmail.com',
      url='http://github.com/braddmiller/pyzcashtools',
      packages=['zcash'],
      scripts=['pyzectool'],
      include_package_data=True,
      data_files=[("", ["LICENSE"]), ("zcash", ["zcash/english.txt"])],
      )
