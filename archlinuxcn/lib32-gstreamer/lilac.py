#!/usr/bin/env python3
from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['patlefort'])
    for line in edit_file('PKGBUILD'):
        line: str
        print(line)
        if line.startswith('build()'):
            print('  export RUSTFLAGS="${RUSTFLAGS// -C link-arg=-Wl,--icf=safe/}"')
