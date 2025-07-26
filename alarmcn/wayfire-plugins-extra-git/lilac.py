from lilaclib import *

def pre_build():
  for line in edit_file('PKGBUILD'):
    if line.startswith('arch='):
      line = 'arch=(aarch64 x86_64)'
    print(line)
