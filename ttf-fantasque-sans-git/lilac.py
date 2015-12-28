from lilaclib import *

build_prefix = 'archlinuxcn-x86_64'

pre_build = vcs_update
depends = ['ttf2eot', 'ttfautohint', 'sfnt2woff']

def post_build():
  git_add_files('PKGBUILD')
  git_commit()

if __name__ == '__main__':
  single_main(build_prefix)
