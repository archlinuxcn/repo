#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build()
    add_provides(['libomxaudio_effects.so', 'libomxclocksrc.so', 'libomxdynamicloader.so', 'libomxil-bellagio.so', 'libomxvideosched.so'])

def post_build():
    aur_post_build()
