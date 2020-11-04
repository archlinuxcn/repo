#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build()
    add_depends(['mjpegtools'])
    add_provides(['liblavfile.so', 'liblavjpeg.so', 'liblavplay.so', 'libmjpegutils.so', 'libmpeg2encpp.so', 'libmplex2.so'])

def post_build():
    aur_post_build()
