from lilaclib import *

build_prefix = 'archlinuxcn-i686'

pre_build = vcs_update

def post_build():
  git_add_files('PKGBUILD')
  git_commit()

if __name__ == '__main__':
  single_main()
