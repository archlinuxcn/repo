from lilaclib import *

def pre_build():
  for line in edit_file('PKGBUILD'):
      if line.startswith('_pkgver'):
          line = "_pkgver=" + _G.newver
      print(line)
  newver = _G.newver.replace("-","")
  update_pkgver_and_pkgrel(newver)

#if __name__ == '__main__':
#  single_main()
