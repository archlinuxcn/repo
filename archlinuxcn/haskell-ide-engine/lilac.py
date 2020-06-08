from lilaclib import *

def pre_build():
  aur_pre_build()

  for line in edit_file('PKGBUILD'):
    if not line.startswith("_enabled_ghc_versions"):
        print(line)
    else:
        print("_enabled_ghc_versions=('8.6.5' '8.8.3')") 

