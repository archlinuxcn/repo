#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build()
    add_depends(['libHalf-2_5.so', 'libIex-2_5.so', 'libIlmImf-2_5.so', 'libWildMidi.so', 'libaom.so', 'libass.so', 'libavtp.so', 'libbs2b.so', 'libchromaprint.so', 'libdc1394.so', 'libdca.so', 'libde265.so', 'libdvdnav.so', 'libdvdread.so', 'libfaac.so', 'libfaad.so', 'libfdk-aac.so', 'libgio-2.0.so', 'libglib-2.0.so', 'libgme.so', 'libgmodule-2.0.so', 'libgobject-2.0.so', 'libgudev-1.0.so', 'libkate.so', 'liblilv-0.so', 'liblrdf.so', 'libmjpegutils-2.1.so', 'libmms.so', 'libmpcdec.so', 'libmpeg2encpp-2.1.so', 'libmplex2-2.1.so', 'libneon.so', 'libnettle.so', 'libnice.so', 'libofa.so', 'libopenjp2.so', 'libpango-1.0.so', 'libpangocairo-1.0.so', 'librsvg-2.so', 'librtmp.so', 'libsbc.so', 'libsndfile.so', 'libspandsp.so', 'libsrt.so', 'libsrtp2.so', 'libusb-1.0.so', 'libwebrtc_audio_processing.so', 'libx265.so', 'libzbar.so', 'libzvbi.so'])
    add_provides(['libgstadaptivedemux-1.0.so', 'libgstbadaudio-1.0.so', 'libgstbasecamerabinsrc-1.0.so', 'libgstcodecparsers-1.0.so', 'libgstcodecs-1.0.so', 'libgstinsertbin-1.0.so', 'libgstisoff-1.0.so', 'libgstmpegts-1.0.so', 'libgstphotography-1.0.so', 'libgstplayer-1.0.so', 'libgstsctp-1.0.so', 'libgsttranscoder-1.0.so', 'libgsturidownloader-1.0.so', 'libgstvulkan-1.0.so', 'libgstwayland-1.0.so', 'libgstwebrtc-1.0.so'])

def post_build():
    aur_post_build()
