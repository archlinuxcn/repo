from types import SimpleNamespace

from lilaclib import *

g = SimpleNamespace()

def pre_build():
  g.files = download_official_pkgbuild('gtk3')
  run_cmd(['patch', '-Np1', 'PKGBUILD', 'pkgbuild.patch'])

def post_build():
  git_add_files(g.files)
  git_commit()
