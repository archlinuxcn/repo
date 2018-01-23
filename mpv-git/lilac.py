#!/usr/bin/env python3
from lilaclib import *
import re

build_prefix = 'archlinuxcn-x86_64'
depends = ['ffmpeg-git']

def pre_build():
    aur_pre_build()
    for line in edit_file('PKGBUILD'):
        if 'depends=(' in line:
            print(line.replace("'ffmpeg'","'ffmpeg-git'"))
        else:
            line=re.sub(r'#(dvd|cd|smb|libarchive|lua$|x11|wayland|uchardet|rubberband|dvbin)',r'\1',line)
            print(line)

post_build = aur_post_build

if __name__ == '__main__':
  single_main(build_prefix)
