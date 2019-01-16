from lilaclib import *

def pre_build():
  newver = _G.newver.split('-', 1)[0]
  update_pkgver_and_pkgrel(newver)

def post_build():
  git_add_files("PKGBUILD")
  git_commit()

if __name__ == '__main__':
  single_main()

