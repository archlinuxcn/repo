#!/usr/bin/env python3

from types import SimpleNamespace

from lilaclib import *

g = SimpleNamespace()

def pre_build():
  g.files = download_official_pkgbuild("gnome-shell")

  state = "out"
  for line in edit_file("PKGBUILD"):
    if line.startswith("pkgbase="):
      line = "_pkgbase=gnome-shell"

    elif line.startswith("pkgname=("):
      line = "pkgname=gnome-shell-everyx"
      state = "pkgname"
    elif state == "pkgname":
      if line.endswith(")"):
          state = "out"
      line = ""

    elif line.startswith("epoch="):
      line = ""

    elif line.startswith("pkgdesc="):
      line = 'provides=("gnome-shell=$pkgver")\n' + 'conflicts=("gnome-shell")\n' +  line[:-1] + ''' (with everyx's patch)"'''

    elif line.startswith("source=("):
      state = "source"
    elif state == "source" and line == ')':
      line = '  "0001-ibus-candidate-popup-support-rime-comment-style.patch"\n' + line
      state = "out"

    elif line.startswith('b2sums='):
      state = 'b2sums'
    elif state == 'b2sums' and line.endswith(')'):
      line = line.replace(')', "\n        'cad4524e03b5a4d7df133c8cc946f9b7cc340cbfe1c8856e91a13d196bf74706519abc9d900bd064d5024146fa19d8a39d970df3d22d92f68f020c28f516ba62')")
      state = 'out'

    elif line.startswith('prepare('):
      state = 'prepare'
    elif state == 'prepare' and line.endswith('}'):
      line = '  git apply -3 "$srcdir"/*.patch\n' + line
      state = 'out'

    elif line.startswith('package_gnome-shell()'):
      line = line.replace("package_gnome-shell()", "package()")

    elif line.startswith('package_gnome-shell-docs()'):
      line = "ignore_" + line.replace("_", "-")

    elif "groups=" in line:
      line = ""

    elif "$pkgbase" in line:
      line = line.replace('$pkgbase', '$_pkgbase')

    print(line)

def post_build():
  git_pkgbuild_commit()
