from lilaclib import *

def pre_build():
  aur_pre_build(maintainers=['kode54'])
  for line in edit_file('PKGBUILD'):
    if line.startswith('arch='):
      line = 'arch=(aarch64 x86_64)'
    print(line)
