from lilaclib import *

def pre_build():
  newver = _G.newver.lstrip('proton-')
  newver = newver.replace("-",".")
  update_pkgver_and_pkgrel(newver)

def post_build():
  git_add_files('PKGBUILD')
  git_commit()
  update_aur_repo()

#if __name__ == '__main__':
#  single_main()
