from lilaclib import *

def pre_build():
  aur_pre_build()

  for line in edit_file('PKGBUILD'):
    if not 'ghc_versions' in line:
        print(line)
    else:
        print("_enabled_ghc_versions=('8.6.5')") 

post_build = aur_post_build

