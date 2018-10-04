#!/usr/bin/env python3

from lilaclib import *

build_prefix = 'extra-x86_64'
update_on = [{'aur':'gnome-shell-extension-topicons-plus-git', 'use_last_modified':True}, {'github':'huttli/TopIcons-plus'}]

def pre_build():
    if str(datetime.datetime.now())[:8] < '20181006':
        run_cmd('rm -rf TopIcons-plus'.split(' '))

    aur_pre_build()

post_build = aur_post_build

if __name__ == '__main__':
  single_main(build_prefix)
