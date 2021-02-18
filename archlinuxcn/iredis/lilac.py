#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    pypi_pre_build(depends = [
        'python',
        'python-redis',
        'python-prompt_toolkit',
        'python-pygments',
        'python-mistune',
        'python-configobj',
        'python-click',
        'python-pendulum',
        'python-importlib_resources',
        'python-wcwidth',
        ], depends_setuptools = False)

def post_build():
    git_add_files('PKGBUILD')
    git_commit()
    update_aur_repo()

