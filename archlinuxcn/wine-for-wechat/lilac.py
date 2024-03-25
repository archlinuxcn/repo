from types import SimpleNamespace
import re

from lilaclib import *

g = SimpleNamespace()

def pre_build():
  g.files = download_official_pkgbuild('wine')

  sums = False

  lib32_re = re.compile(r'\s+lib32-[\S]+')
  ignore_until = None
  ignore_count = 1

  for line in edit_file('PKGBUILD'):
    line = lib32_re.sub('', line)
    if '$pkgname' in line:
      line = line.replace('$pkgname', '$_pkgname')

    if ignore_until:
      if ignore_until.fullmatch(line):
        if ignore_count == 1:
          ignore_until = None
        else:
          ignore_count -= 1
          continue
      else:
        continue

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
    elif line.strip() == '--enable-win64':
      line += ' \\\n    --enable-archs=x86_64,i386\n'
      ignore_until = re.compile(r'\s*make\s*')
      ignore_count = 2
    elif line.startswith('package()'):
      ignore_until = re.compile(r'.*Wine-64.*')

    print(line)

def post_build():
  git_add_files(g.files)
  git_commit()
