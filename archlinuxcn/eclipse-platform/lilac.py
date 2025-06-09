#!/usr/bin/env python3

import os
from datetime import datetime
import time

from lilaclib import *

build_prefix = 'extra-x86_64'

def pre_build():
    aur_pre_build(maintainers=['BochengZou'])

    html = subprocess.check_output(
        ['curl', '-fsSL', 'https://download.eclipse.org/eclipse/downloads/index.html']
    )
    text = html.decode('utf-8', errors='ignore')

    m = re.search(r'R-([0-9]+\.[0-9]+)-([0-9]{12})', text)
    if not m:
        raise RuntimeError("Could not find Eclipse release marker in HTML")
    ver, _ver = m.group(1), m.group(2)

    for line in edit_file('PKGBUILD'):
        if line.startswith('_pkgver='):
            line = f'_pkgver="{_ver}"'
        print(line)

    update_pkgver_and_pkgrel(ver)
    run_cmd(['updpkgsums'])

def post_build():
    git_add_files('PKGBUILD')
    git_commit()

if __name__ == '__main__':
  single_main()
