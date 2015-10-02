from lilaclib import *

build_prefix = 'extra-x86_64'

pre_build = vcs_update
depends = ['python-alembic', 'python-editor']

def post_build():
  git_add_files('PKGBUILD')
  git_commit()

if __name__ == '__main__':
  single_main()
