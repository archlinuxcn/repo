from lilaclib import *

build_prefix = 'extra-x86_64'

depends = ['lxqt-build-tools-git']

def post_build():
    git_add_files('PKGBUILD')
    git_commit()

pre_build = vcs_update

if __name__ == '__main__':
    single_main(build_prefix)
