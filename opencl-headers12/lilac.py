from lilaclib import *

pre_build = vcs_update

def post_build():
    git_add_files('PKGBUILD')
    mkaurball()
    git_commit()

if __name__ == '__main__':
    single_main('archlinuxcn-i686')
    single_main('archlinuxcn-x86_64')
