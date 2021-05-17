from lilaclib import *

def pre_build():
  newver = _G.newver.removeprefix('release-')
  for line in edit_file('PKGBUILD'):
      if line.startswith('_pkgver'):
          line = "_pkgver='" + newver + "'"
      print(line)

  newver = newver.replace("-",".")
  update_pkgver_and_pkgrel(newver)

#if __name__ == '__main__':
#  single_main()
