#!/usr/bin/python3

from lilaclib import *

def pre_build():
    for line in edit_file('PKGBUILD'):
        if '${_processor_opt:=}' in line:
            line = line.replace('_processor_opt:=', '_processor_opt:=generic')
        print(line)
