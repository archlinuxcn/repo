# Trimmed lilac.py
#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *
import glob

#build_prefix = 'extra-x86_64'

_g = SimpleNamespace()

def pre_build():
  if os.path.exists('PKGBUILD'):
    pkgver, pkgrel = get_pkgver_and_pkgrel()
  else:
    pkgver = None

  _g.aur_pre_files = clean_directory()
  name = os.path.basename(os.getcwd())
  aur_building_files = download_aur_pkgbuild(name)
  # remove .* file from aur
  aur_building_files = [x for x in aur_building_files if x not in glob.glob(".*")]
  _g.aur_building_files = aur_building_files

  new_pkgver = get_pkgver_and_pkgrel()[0]
  if pkgver and pkgver == new_pkgver:
    # change pkgrel to what specified in PKGBUILD
    update_pkgrel(pkgrel)

  if name.endswith(('-git', '-hg', '-svn', '-bzr')):
    vcs_update()

def post_build():
  git_rm_files(_g.aur_pre_files)
  git_add_files(_g.aur_building_files)
  output = run_cmd(["git", "status", "-s", "."]).strip()
  if output:
    git_commit()
  del _g.aur_pre_files, _g.aur_building_files


#if __name__ == '__main__':
#    single_main(build_prefix)

