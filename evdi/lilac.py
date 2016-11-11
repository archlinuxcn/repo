#!/usr/bin/python3

from lilaclib import *

build_prefix = 'extra-x86_64'

import re

def get_item(s):
    m = re.search(r'''[ \t'"]*([^ '"]+)[ \t'"]*''', s)
    if m != None:
        return m.group(1)
    else:
        return None

def add_into_array(line, values):
    l = line.find('(')
    r = line.rfind(')')
    arr_str = line[l+1:r].strip()
    arr = {get_item(x) for x in arr_str.split(' ')}.union(values)
    arr_str = '('
    for item in arr:
        if item == None: continue
        arr_str += "'{}' ".format(item)
    arr_str += ')'
    line = line[:l] + arr_str
    return line

def pre_build():
    aur_pre_build()
    for line in edit_file('PKGBUILD'):
        if line.strip().startswith('makedepends'):
            makedeps = ['linux', 'linux-headers']
            line = add_into_array(line, makedeps)
        if line.strip().startswith('depends'):
            makedeps = ['libdrm']
            line = add_into_array(line, makedeps)
        print(line)

post_build = aur_post_build

if __name__ == '__main__':
    single_main()

