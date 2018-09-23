#!/usr/bin/env python3

from lilaclib import *

build_prefix = 'extra-x86_64'

update_on = [{'pypi': 'sniffio'}]

def pre_build():
  pypi_pre_build(
    depends=[],
    depends_setuptools=False)

def post_build():
  git_add_files('PKGBUILD')
  git_commit()
  update_aur_repo()

if __name__ == '__main__':
  single_main()
