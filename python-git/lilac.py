from lilaclib import *

build_prefix = 'extra-x86_64'
time_limit_hours = 1.5

def post_build():
    git_add_files('PKGBUILD')
    git_commit()

pre_build = vcs_update

if __name__ == '__main__':
    single_main(build_prefix)
