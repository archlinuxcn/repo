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
             '  "0002-message-tray-add-timeout-watchdog-for-notification-hiding-animation.patch"\n' + \
             line
      state = "out"

    elif line.startswith('b2sums='):
      state = 'b2sums'
    elif state == 'b2sums' and line.endswith(')'):
      line = line.replace(')', 
                          "\n        'c9cb3d42cdbb16322b170268b7a18ba7156ed1839525c6a6398d286d55aab15720dee17442ce103e2d8521a335046b5137d2b182113e1e72ff4477cea3c55594'" + \
                          "\n        'a95c44fd46bc51db91ec5867dc93b550cfef630113f63545555dfaa779b972bc2bea6c60c349abf5ac76c942e481d80b9f4fbd84c779a3907a17f2d32a10e72f'" + \
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
