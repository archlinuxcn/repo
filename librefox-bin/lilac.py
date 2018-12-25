#!/usr/bin/env python3

from lilaclib import *

build_prefix = 'extra-x86_64'


def pre_build():
    # do something after successful build
    url, ver, firefox_ver = s.head(
        "https://github.com/intika/Librefox/releases/latest").headers['Location'].split("-v")
    for line in edit_file('PKGBUILD'):
        if 'pkgver=' in line:
            line = 'pkgver='+ver
        if '_firefox_ver=' in line:
            line = '_firefox_ver'+firefox_ver
        print(line)

    run_cmd(['updpkgsums'])


def post_build():
    git_add_files('PKGBUILD')
    git_commit()


if __name__ == '__main__':
    single_main()
