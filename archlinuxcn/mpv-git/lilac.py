#!/usr/bin/env python3
from lilaclib import *
import re

update_on = [{'aur':None}, {'github':'mpv-player/mpv'}, {'vcs':'git+https://git.ffmpeg.org/ffmpeg.git'}]
repo_depends = ['ffmpeg-git']
build_prefix = 'extra-x86_64'

def pre_build():

    old_pkgver, old_pkgrel = get_pkgver_and_pkgrel()
    run_cmd(['rm', '-f', 'PKGBUILD'])

    aur_pre_build()

    new_pkgver, new_pkgrel = get_pkgver_and_pkgrel()
    if old_pkgver == new_pkgver and new_pkgrel <= old_pkgrel:
        update_pkgrel(old_pkgrel+1)

    for line in edit_file('PKGBUILD'):
        if 'depends=(' in line:
            print(line)
        else:
            line=re.sub(r'#(dvd|cd|smb|libarchive|lua$|x11|wayland|uchardet|rubberband|dvbin|vulkan|shaderc)',r'\1',line)
            print(line)

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
