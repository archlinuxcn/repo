#!/usr/bin/env python3

import os
from datetime import datetime
import time
import json

from lilaclib import *

build_prefix = 'extra-x86_64'

def pre_build():
    data = subprocess.check_output(
        ['curl', '-fsSL', 'https://download.eclipse.org/eclipse/downloads/data.json']
    ).decode('utf-8', errors='ignore')

    j = json.loads(data)

    # Pick the first successful release entry (fallback to first entry)
    rel = next((x for x in j.get('releases', []) if x.get('status') == 'success'),
               j['releases'][0])

    ver = rel['label']              # e.g. "4.38"
    path = rel['path']              # e.g. "drops4/R-4.38-202512010920"
    drop_dir = path.rstrip('/').split('/')[-1]  # "R-4.38-202512010920"

    parts = drop_dir.split('-')
    if len(parts) >= 3 and parts[0] == 'R':
        _ver = parts[2]             # e.g. "202512010920"
    else:
        m = re.search(r'R-[0-9]+\.[0-9]+-([0-9]{12})', drop_dir)
        if not m:
            raise RuntimeError(f"Could not parse Eclipse release timestamp from path: {path}")
        _ver = m.group(1)

    print("_ver = " + _ver)

    for line in edit_file('PKGBUILD'):
        if line.startswith('_pkgbuild='):
            line = f'_pkgbuild="{_ver}"'
        print(line)

    update_pkgver_and_pkgrel(ver)
    run_cmd(['updpkgsums'])

def post_build():
    git_add_files('PKGBUILD')
    git_commit()

if __name__ == '__main__':
  single_main()
