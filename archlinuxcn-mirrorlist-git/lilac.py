from lilaclib import *

build_prefix = 'extra-x86_64'

def pre_build():
  run_cmd(["rm", "-rf", "mirrorlist-repo"])
  vcs_update()

def post_build():
  git_add_files('PKGBUILD')
  git_commit()

if __name__ == '__main__':
  single_main(build_prefix)
