from lilaclib import *

def pre_build():
  aur_pre_build(maintainers=['CyberShadow'])
  for l in edit_file('PKGBUILD'):
    if l.startswith('depends='):
      # not any d-runtime works; it works only with the one used for building
      l = l.replace("'d-runtime'", "'liblphobos'")
    print(l)
