from lilaclib import *

def pre_build():
  
  for line in edit_file('PKGBUILD'):
    if line.startswith('_srctag='):
      line = '_srctag=' + _G.newver
    print(line)

def post_build():
  git_pkgbuild_commit()
