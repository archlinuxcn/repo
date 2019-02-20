#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    pypi_pre_build(
        depends = ['python-bleach', 'python-jinja', 'python-werkzeug', 'python-html5lib-9x07', 'python-misaka', 'python-itsdangerous', 'python-six', 'python-cffi', 'sqlite'],
        depends_setuptools = True,
        arch = ['any']
    )

def post_build():
    pypi_post_build()
    update_aur_repo()
