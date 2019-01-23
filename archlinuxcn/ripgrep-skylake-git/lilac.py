from lilaclib import *

pre_build = vcs_update

def post_build():
  git_pkgbuild_commit()

if __name__ == '__main__':
  single_main()
