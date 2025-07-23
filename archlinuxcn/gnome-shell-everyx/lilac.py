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
      line = line.replace(')', "\n        'a99cc3a412e85435cf766ed4c34842f4840cef3072dc669d6e595219398824ebc74e7bce489d7aa150c0dbaa231560122f7694c88358fb187289201fbe0904b9')")
      state = 'out'

    elif line.startswith('prepare='):
      state = 'prepare'
    elif state == 'prepare' and line.endswith('}'):
      line = '  git apply -3 "$srcdir"/*.patch\n' + line
      state = 'out'

    elif line.startswith('package_gnome-shell()'):
      line = line.replace("package_gnome-shell()", "package()")

    elif line.startswith('package_gnome-shell-docs()'):
      line = "no" + line

    elif "groups=" in line:
      line = ""

    elif "$pkgbase" in line:
      line = line.replace('$pkgbase', '$_pkgbase')

    print(line)

def post_build():
  git_add_files(g.files)
  git_commit()
