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
      line = '  "0001-ibus-candidate-popup-support-rime-comment-style.patch"\n' + \
             '  "0002-messageTray-Add-timeout-watchdog-for-notification-hi.patch"\n' + \
             line
      state = "out"

    elif line.startswith('b2sums='):
      state = 'b2sums'
    elif state == 'b2sums' and line.endswith(')'):
      line = line.replace(')', 
                          "\n        'd462269fe9894d44ec6a2b5a030010ce16aaee5cebdd79c9d1817c4e5bbf054f9cc0da2e8048e1e09828645e142c3cab664d119f922b597c8b19f7687358e7b4'" + \
                          "\n        'cb4c20a87eb17de850d2e16e31f9acd4d4d5a5d5cd4d31c6d57627f2d67391b4d5d85c8b545ee188826609a0eee8d0bb57fb8249e48e08c15112d9aba4ad4ffa'" + \
                          ")")
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
