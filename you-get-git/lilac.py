from lilaclib import *

build_prefix = 'extra-x86_64'

def pre_build():
  run_cmd(['makepkg', '-o'])
  output = run_cmd(["git", "status", "-s", "PKGBUILD"]).strip()
  if not output:
    raise RuntimeError('no update available. something goes wrong?')

def post_build():
  git_add_files('PKGBUILD')
  git_commit()

if __name__ == '__main__':
  single_main()
