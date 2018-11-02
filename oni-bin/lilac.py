#!/usr/bin/env python3

from lilaclib import *

build_prefix = 'extra-x86_64'


def pre_build():
    _betaver = _G.newver.lstrip('v')

    pkgver, pkgrel = get_pkgver_and_pkgrel()

    for line in edit_file('PKGBUILD'):
        if line.startswith('_betaver=') and pkgver != _betaver.replace('-', ''):
            line = f'_betaver={_betaver}'
        elif line.startswith('pkgrel='):
            if pkgver != _betaver.replace('-', ''):
                line = 'pkgrel=1'
            else:
                line = f'pkgrel={int(pkgrel)+1}'
    print(line)

    run_cmd(['updpkgsums'])


def post_build():
    git_add_files('PKGBUILD')
    git_commit()
    update_aur_repo()


if __name__ == '__main__':
    single_main()
