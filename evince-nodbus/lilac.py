#!/usr/bin/env python3

import fileinput
from types import SimpleNamespace

from lilaclib import *

g = SimpleNamespace()

build_prefix = 'extra-x86_64'

def pre_build():
  g.oldfiles = clean_directory()
  g.files = download_official_pkgbuild('evince')

  with fileinput.input(files=('PKGBUILD',), inplace=True) as f:
    for line in f:
      line = line.rstrip('\n')
      if line.startswith('pkgname='):
        line = 'pkgname=evince-nodbus'
      elif '$pkgname' in line:
        line = line.replace('$pkgname', 'evince')
      elif line.startswith('groups='):
        line = line + '''\nconflicts=('evince')\nprovides=("evince=$pkgver")\n'''
      elif '--enable-introspection' in line:
        line += '  --disable-dbus'
      elif line.strip() == 'make':
        line = '''  sed -i '/"win.reload",/a          "win.show-properties",	"<Alt>Return", NULL,' shell/ev-application.c\n''' + line
      print(line)

def post_build():
  git_rm_files(g.oldfiles)
  git_add_files(g.files)
  git_commit()

if __name__ == '__main__':
  single_main()
