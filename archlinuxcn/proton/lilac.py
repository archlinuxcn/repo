from lilaclib import *

def pre_build():
  newver = _G.newver.removeprefix('proton-')
  for line in edit_file('PKGBUILD'):
      if line.startswith('_pkgver'):
          line = "_pkgver='" + newver + "'"
      print(line)

  newver = newver.replace("-",".")
  update_pkgver_and_pkgrel(newver)

def post_build():
  git_add_files('PKGBUILD')
  git_commit()

#if __name__ == '__main__':
#  single_main()
