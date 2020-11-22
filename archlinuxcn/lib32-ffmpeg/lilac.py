#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build()
    add_depends(['libaom.so', 'libasound.so', 'libass.so', 'libbluray.so', 'libdav1d.so', 'libfontconfig.so', 'libfreetype.so', 'libfribidi.so', 'libgsm.so', 'libjack.so', 'libmp3lame.so', 'libopencore-amrnb.so', 'libopencore-amrwb.so', 'libopenjp2.so', 'libsrt.so', 'libvmaf.so', 'libvorbis.so', 'libvorbisenc.so', 'libvpx.so', 'libx264.so', 'libx265.so', 'libxvidcore.so'])

def post_build():
    aur_post_build()
