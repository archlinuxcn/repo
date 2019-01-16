#!/usr/bin/env python3

from lilaclib import *

def pre_build():
  pypi_pre_build(depends=['python', 'mpv', 'python-beautifulsoup4', 'python-marshmallow', 'python-pycrypto', 'python-requests', 'python-mutagen', 'python-fuzzywuzzy', 'python-setuptools'], license='MIT')

def post_build():
  pypi_post_build()
