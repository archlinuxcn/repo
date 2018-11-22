#!/usr/bin/env python3
from lilaclib import *

update_on = [{'aur':None}]
build_prefix = 'extra-x86_64'

def pre_build():
  aur_pre_build()

  for line in edit_file('PKGBUILD'):
    if 'java-runtime' in line:
        print(line.replace('java-runtime','java-environment'))
    elif 'gradle jar' in line:
        print('\tmkdir gradle-cache')
        print('\texport GRADLE_USER_HOME="${srcdir}/${pkgname}/gradle-cache"')
        print(line)
    elif 'changelog=.CHANGELOG' in line:
        print('#'+line)
    else:
        print(line)

def post_build():
  git_add_files('PKGBUILD')
  git_add_files('opsu.sh')
  git_commit()

if __name__ == '__main__':
    single_main(build_prefix)
