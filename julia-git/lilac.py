from lilaclib import *

build_prefix = 'extra-x86_64'
depends = ['libunwind-git', 'llvm-julia', 'openspecfun-git',
           'openblas-lapack-git', 'libutf8proc-git']

pre_build = vcs_update

def post_build():
  git_add_files('PKGBUILD')
  git_commit()

if __name__ == '__main__':
  single_main()
