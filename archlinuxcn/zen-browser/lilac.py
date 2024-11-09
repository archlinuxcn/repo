#!/usr/bin/python3
from lilaclib import *

# TODO: Auto update `_languages`
# TODO: Auto update `firefox-l10n`
def pre_build():
    resp = s.get(f"https://raw.githubusercontent.com/zen-browser/desktop/refs/tags/{_G.newver}/surfer.json")
    firefox_version = resp.json()["version"]["version"]

    for line in edit_file('PKGBUILD'):
        if line.startswith('_firefox_version='):
            line = f"_firefox_version={firefox_version}"
        print(line)

    update_pkgver_and_pkgrel(_G.newver.replace('-', '_'))
