from lilaclib import *

build_prefix = 'archlinuxcn-x86_64'

def pre_build():
    newver = _G.newver
    oldver = _G.oldver
    for line in edit_file('PKGBUILD'):
        if line.startswith('pkgver='):
            line = 'pkgver=' + newver
        elif line.startswith('pkgrel=') and newver != oldver:
            line = 'pkgrel=1'
        print(line)

def post_build():
    git_add_files('PKGBUILD')
    git_commit()

if __name__ == '__main__':
    _G = SimpleNamespace(oldver=OLD_VER, newver=NEW_VER)
    single_main(build_prefix)
