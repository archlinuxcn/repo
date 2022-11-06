#!/usr/bin/env python3
from lilaclib import *

def _get_new_version():
  new_verion = s.get("https://api.github.com/repos/concourse/concourse/tags").json()[0]
  return new_verion['name']

def pre_build():
  aur_pre_build(maintainers=['lilac', 'Sasasu'])
  ver = _get_new_version()
  for l in edit_file('PKGBUILD'):
    if l.startswith('pkgver='):
      l = 'pkgver=' + ver
    print(l)
  run_cmd(["updpkgsums"])

def post_build():
  aur_post_build()
  git_add_files("PKGBUILD")
  git_commit()
  update_aur_repo()

