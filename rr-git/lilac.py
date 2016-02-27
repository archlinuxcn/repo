from lilaclib import *

build_prefix = 'multilib-archlinuxcn'

pre_build = vcs_update

def post_build():
    git_add_files('PKGBUILD')
    git_commit()

if __name__ == '__main__':
    single_main(build_prefix)
