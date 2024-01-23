#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    pypi_pre_build(
        makedepends = [
            'python-setuptools',
            'python-build',
            'python-installer',
            'python-wheel',
            'python-poetry',
        ], depends = [
            'python',
            'python-redis',
            'python-packaging',
            'python-prompt_toolkit',
            'python-pygments',
            'python-mistune',
            'python-configobj',
            'python-click',
            'python-pendulum',
        ], depends_setuptools = False)

def post_build():
    git_add_files('PKGBUILD')
    git_commit()
    update_aur_repo()

