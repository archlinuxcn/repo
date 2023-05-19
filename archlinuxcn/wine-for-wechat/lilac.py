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
      line = line.replace(')', "\n            '646dfd6ec62fb9ddbfb27aac0ac80d87926fbc3360bb53cca942622e95d1ec380f0b5efdfd45bbe1cdce72661b7b36b15ffb7874b1b4269e3bd56a14ec0d2166')")
      sums = False
    elif line.startswith('install='):
      line += '\nprovides=(wine=$pkgver)\nconflicts=(wine)'
    elif line.startswith('  mv '):
      line += '\n  (cd $_pkgname && patch -p1 < ../wine-wechat.patch)'

    print(line)

def post_build():
  git_add_files(g.files)
  git_commit()
