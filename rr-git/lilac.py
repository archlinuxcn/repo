from lilaclib import *

build_prefix = 'multilib-archlinuxcn'
depends = ['libpfm4-git']

pre_build = vcs_update

def post_build():
    git_add_files('PKGBUILD')
    git_commit()

if __name__ == '__main__':
    single_main(build_prefix)
