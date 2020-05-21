from types import SimpleNamespace

from lilaclib import *

g = SimpleNamespace()

def pre_build():
  g.files = download_official_pkgbuild('wine')

  sums = False

  for line in edit_file('PKGBUILD'):
    if '$pkgname' in line:
      line = line.replace('$pkgname', '$_pkgname')

    if line.startswith('pkgname='):
      line = '_pkgname=wine\npkgname=wine-for-wechat'
    elif line.endswith('wine-binfmt.conf)'):
      line = line.replace(')', ' wine-wechat.patch)')
    elif line.startswith('pkgdesc='):
      line = 'pkgdesc="A patched version of Wine for running Wechat and Netease Music without persistent shadow windows"'
    elif line.startswith('sha512sums=('):
      sums = True
    elif sums and line.endswith("')"):
      line = line.replace(')', "\n            '58670e99749e9f6157171ec186c195f8e21824d49c8ef97613b4c50a2853849297d553458567893fc6792159de2c4b0dede9a0abfc606e4c22249b8b4a84643d')")
      sums = False
    elif line.startswith('install='):
      line += '\nprovides=(wine=$pkgver)\nconflicts=(wine)'
    elif line.startswith('  mv '):
      line += '\n  (cd $_pkgname && patch -p1 < ../wine-wechat.patch)'

    print(line)

def post_build():
  git_add_files(g.files)
  git_commit()
