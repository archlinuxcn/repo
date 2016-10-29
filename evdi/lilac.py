#!/usr/bin/python3

from lilaclib import *

build_prefix = 'extra-x86_64'

def add_into_array(line, values):
    l = line.find('(')
    r = line.rfind(')')
    arr_str = line[l+1:r].strip()
    if arr_str == '':
        arr = []
    else:
        arr = [x.strip().strip('"').strip("'") for x in arr_str.split(',')]
    for dep in values:
        if line.find(dep) == -1:
            arr.append(dep)
    line = line[:l] + arr.__str__().replace('[','(',1).replace(']',')',1)
    return line

def pre_build():
    aur_pre_build()
    for line in edit_file('PKGBUILD'):
        if line.strip().startswith('makedepends'):
            makedeps = ['linux-headers']
            line = add_into_array(line, makedeps)
        print(line)

post_build = aur_post_build

if __name__ == '__main__':
    single_main()

