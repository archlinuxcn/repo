from lilaclib import *

def pre_build():
  for line in edit_file('PKGBUILD'):
      if line.startswith('_pkgver'):
          line = f'_pkgver={_G.newver}'
      print(line)

#if __name__ == '__main__':
#  single_main()
