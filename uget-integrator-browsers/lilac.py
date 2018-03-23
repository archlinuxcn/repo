#!/usr/bin/env python3
from lilaclib import *

build_prefix = 'archlinuxcn-x86_64-build'

def _get_new_version():
  new_verion = s.get("https://api.github.com/repos/ugetdm/uget-integrator/tags").json()[0]
  return new_verion['name'][1:]

def pre_build():
  ver = _get_new_version()
  for l in edit_file('PKGBUILD'):
    if l.startswith('pkgver='):
      l = 'pkgver=' + ver
    print(l)
  run_cmd(["updpkgsums"])

def post_build():
  git_add_files("PKGBUILD")
  git_commit()
  update_aur_repo()

if __name__ == '__main__':
  single_main()
