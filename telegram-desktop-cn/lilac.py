#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *

depends=["libunity", ("libappindicator", "libappindicator-gtk2")]

PATCH=b"""
diff --git a/telegram-desktop-cn/PKGBUILD b/telegram-desktop-cn/PKGBUILD
index 63ea9d9..4877aeb 100644
--- a/telegram-desktop-cn/PKGBUILD
+++ b/telegram-desktop-cn/PKGBUILD
@@ -6,7 +6,7 @@ pkgdesc='fixed The Official desktop version of Telegram messaging app with supor
 arch=('i686' 'x86_64')
 url="https://desktop.telegram.org/"
 license=('GPL3')
-depends=(fontconfig icu jasper libexif libjpeg-turbo libmng libsm libwebp libxi libxkbcommon-x11 mesa mtdev openal opusfile fcitx)
+depends=(fontconfig icu jasper libexif libjpeg-turbo libmng libsm libwebp libxi libxkbcommon-x11 mesa mtdev openal opusfile fcitx ffmpeg)
 makedepends=(git libunity libappindicator-gtk2 xorg-server-xvfb)
 source=(http://download.qt-project.org/official_releases/qt/${_qtver%.*}/$_qtver/single/qt-everywhere-opensource-src-$_qtver.tar.xz
         git+https://github.com/aphuse/tdesktop.git)
"""

build_prefix = 'extra-x86_64'
post_build = aur_post_build


import subprocess

def apply_patch(filename, patch):
    patch_proc = subprocess.Popen(["patch", "-p1", filename], stdin=subprocess.PIPE)
    patch_proc.communicate(patch)

def pre_build():
    aur_pre_build()
    apply_patch("PKGBUILD", PATCH)

if __name__ == '__main__':
    single_main(build_prefix)

