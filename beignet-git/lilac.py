from lilaclib import *

build_prefix = ['archlinuxcn-i686', 'archlinuxcn-x86_64']

pre_build = lambda: run_cmd(['makepkg', '-o'], use_pty=True)

def post_build():
    git_add_files('PKGBUILD')
    mkaurball()
    git_commit()

if __name__ == '__main__':
    single_main(build_prefix)
