#!/usr/bin/python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['severach'])
    for line in edit_file('PKGBUILD'):
        if line.startswith('depends='):
            line = line.replace('pulseaudio', 'pulse-native-provider')
        print(line)
