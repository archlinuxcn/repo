from types import SimpleNamespace

from lilaclib import *

g = SimpleNamespace()

def pre_build():
  g.files = download_official_pkgbuild('gtk3')
  run_cmd(['patch', '-Np1', 'PKGBUILD', 'pkgbuild.patch'])
  for l in edit_file('PKGBUILD'):
    if l.startswith('package_gtk3-demos'):
      break
    print(l)

def post_build():
  git_add_files(g.files)
  git_commit()
