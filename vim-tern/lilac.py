#!/usr/bin/env python3
from lilaclib import *

update_on = [{'aur':None}, {'github':'ternjs/tern_for_vim'}]
build_prefix = 'extra-x86_64'

def pre_build():
    if str(datetime.datetime.now())[:8] < '20180604':
        run_cmd('rm -rf tern_for_vim'.split(' '))

    aur_pre_build()

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
