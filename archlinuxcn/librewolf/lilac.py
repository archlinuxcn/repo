from lilaclib import *
import re

def pre_build():
  newver_upstream = _G.newvers[0].removeprefix('v')
  newver_true = newver_upstream.replace("-","_")
  newver_real = re.sub(r'-.*',"",newver_upstream)
  newver_settings = _G.newvers[1].removeprefix('v')
  for line in edit_file('PKGBUILD'):
      if line.startswith('_pkgver'):
          line = "_pkgver='" + newver_upstream + "'"
      elif line.startswith('_pkgver_real'):
          line = "_pkgver_real='" + newver_real + "'"
      elif line.startswith('_settings_tag'):
          line = "_settings_tag='" + newver_settings + "'"
      print(line)
  update_pkgver_and_pkgrel(newver_true)

#if __name__ == '__main__':
#  single_main()
