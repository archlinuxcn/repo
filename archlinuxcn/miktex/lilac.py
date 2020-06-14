from lilaclib import *

def pre_build():
  update_pkgver_and_pkgrel()

def post_build():
  git_add_files('PKGBUILD')
  git_commit()
  update_aur_repo()

#if __name__ == '__main__':
#  single_main()
