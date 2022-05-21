#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build()
    for line in edit_file('PKGBUILD'):
        if line.endswith('"$pkgdir/usr/lib/firefox-esr/extensions/langpack-$1@firefox.mozilla.org.xpi"'):
            line = ('    '
                    '"$pkgdir/usr/lib/firefox-esr/browser/extensions/langpack-$1@firefox.mozilla.org.xpi"')
        print(line)
