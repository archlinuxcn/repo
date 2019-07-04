#!/usr/bin/python3

from lilaclib import *

def pre_build():

    aur_pre_build()
    
    for line in edit_file('PKGBUILD'):
        if line.strip().startswith('local _flags=('):
            print(line)
            print("    'use_jumbo_build = true'")
        else:
            print(line)
    
    run_cmd(["updpkgsums"])


#if __name__ == '__main__':
#    single_main('extra-x86_64')

