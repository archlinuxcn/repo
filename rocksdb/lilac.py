#!/usr/bin/env python3

from lilaclib import *

build_prefix = 'extra-x86_64'


pre_build = aur_pre_build
post_build = aur_post_build

def pre_build():
    aur_pre_build()
    for line in edit_file('PKGBUILD'):
        if line.startswith('source='):
            line = line.replace(')', ' "fix3870.patch::https://github.com/facebook/rocksdb/commit/e5ae1bb46564689e56a38f3509daffa4aca3b29c.patch"')
        if line.startswith('sha256sums=)'):
            line = line.replace(')', " '0f92592afece0a0ad743721472a1d5a8c714d7564463db04c547382cf40454d9')")
        print(line)

if __name__ == '__main__':
    single_main(build_prefix)
