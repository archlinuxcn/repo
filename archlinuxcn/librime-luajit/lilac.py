from types import SimpleNamespace

from lilaclib import *

g = SimpleNamespace()


def pre_build():
    g.files = download_official_pkgbuild('librime')

    for line in edit_file('PKGBUILD'):
        if line.startswith('pkgname='):
            line = 'pkgname=librime-luajit'
        elif line.startswith('depends=('):
            line = line.replace("'lua'", "'luajit'", 1)
        elif line.startswith('arch=('):
            print(line)
            print('provides=("librime=$pkgver")')
            print('conflicts=(librime)')
            continue
        elif '-DENABLE_EXTERNAL_PLUGINS=On' in line:
            line = f'{line} -DLUA_VERSION=luajit'
        print(line)


def post_build():
    git_add_files(g.files)
    git_commit()
