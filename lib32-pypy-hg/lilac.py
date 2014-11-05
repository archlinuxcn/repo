from lilaclib import *

build_prefix = ['multilib-archlinuxcn']

pre_build = lambda: run_cmd(['makepkg', '-o'], use_pty=True)

def post_build():
    git_add_files('PKGBUILD')
    mkaurball()
    git_commit()

if __name__ == '__main__':
    single_main(build_prefix)
