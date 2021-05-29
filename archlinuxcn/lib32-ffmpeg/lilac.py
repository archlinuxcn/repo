#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers='oxalin')
    depends = ' '.join(['libaom.so', 'libasound.so', 'libass.so', 'libbluray.so', 'libdav1d.so', 'libfontconfig.so', 'libfreetype.so', 'libfribidi.so', 'libgsm.so', 'libjack.so', 'libmp3lame.so', 'libopencore-amrnb.so', 'libopencore-amrwb.so', 'libopenjp2.so', 'libsrt.so', 'libvmaf.so', 'libvorbis.so', 'libvorbisenc.so', 'libvpx.so', 'libx264.so', 'libx265.so', 'libxvidcore.so'])
    done = False
    for line in edit_file('PKGBUILD'):
        if not done and line.strip().startswith('depends='):
            pos = line.find('(') + 1
            print(f'{line[:pos]}{depends} {line[pos:]}')
            done = True
        else:
            print(line)

def post_build():
    check_library_provides()
    aur_post_build()
