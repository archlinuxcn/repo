#!/usr/bin/env python3
from lilaclib import *

update_on = [{'aur':None}]
build_prefix = 'archlinuxcn-x86_64'
depends = ['qt-installer-framework']

def pre_build():
    run_cmd(["rm", "-f", "eula.html"])
    aur_pre_build()

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
