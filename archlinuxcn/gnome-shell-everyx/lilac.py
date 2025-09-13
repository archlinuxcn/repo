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
             '  "0002-messageTray-Fix-race-condition-causing-stuck-notific.patch"\n' + \
             line
      state = "out"

    elif line.startswith('b2sums='):
      state = 'b2sums'
    elif state == 'b2sums' and line.endswith(')'):
      line = line.replace(')', 
                          "\n        '151a4ad7f50dd2946fe8bef074e79e21dad78591b0624993b41cce64cb0ef0e7766d17f018bec878b105df5ed7d886efc7a0f7b49c13de3c8e8bcfabd78c1114'" + \
                          "\n        'e54d3c5b5a8db1439287a2f3ebdbcd8bd66d500498b19dda02cb5813fe0a08a15e885cbd2114dc7262159ea253750b7e825915220c02249571e6225fe209c54f'" + \
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
