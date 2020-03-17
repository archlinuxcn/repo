#!/usr/bin/env python3
from lilaclib import *

update_on = [{'aur':None}, {'github':'aleho/gnome-shell-volume-mixer'}]
build_prefix = 'extra-x86_64'

def pre_build():
    aur_pre_build()
    run_cmd('wget -O 1521.patch https://patch-diff.githubusercontent.com/raw/archlinuxcn/repo/pull/1521.patch'.split(' '))
    run_cmd('patch -p3 < 1521.patch')

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
