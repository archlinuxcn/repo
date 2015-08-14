#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *

depends = ['libunity', ('libappindicator', 'libappindicator-gtk2')]

build_prefix = 'extra-x86_64'

PATCH = b"""
diff --git a/telegram-desktop-git/PKGBUILD b/telegram-desktop-git/PKGBUILD
index 29f48f3..38f78fe 100644
--- a/telegram-desktop-git/PKGBUILD
+++ b/telegram-desktop-git/PKGBUILD
@@ -9,7 +9,7 @@ license=('GPL3')
 depends=(ffmpeg icu jasper libexif libmng libwebp libxkbcommon-x11 mtdev openal)
 makedepends=(git libunity libappindicator-gtk2 xorg-server-xvfb)
 source=("http://download.qt-project.org/official_releases/qt/${_qtver%.*}/$_qtver/single/qt-everywhere-opensource-src-$_qtver.tar.gz"
-        'tdesktop::git+https://github.com/telegramdesktop/tdesktop.git#branch=dev')
+        'tdesktop::git+https://github.com/telegramdesktop/tdesktop.git#branch=master')

 pkgver() {
   cd "tdesktop"
@@ -29,6 +29,7 @@ prepare() {
   fi

   sed -i 's/CUSTOM_API_ID//g' "$srcdir"/tdesktop/Telegram/Telegram.pro
+  sed -i 's/LIBS += \/usr\/local\/lib\/libxkbcommon.a//g' "$srcdir"/tdesktop/Telegram/Telegram.pro

   (
     echo 'INCLUDEPATH += "/usr/lib/glib-2.0/include"'
"""

import subprocess

def apply_patch(filename, patch):
    patch_proc = subprocess.Popen(["patch", "-p1", filename], stdin=subprocess.PIPE)
    patch_proc.communicate(patch)

def pre_build():
    aur_pre_build()
    apply_patch("PKGBUILD", PATCH)

post_build = aur_post_build

if __name__ == '__main__':
  single_main(build_prefix)


