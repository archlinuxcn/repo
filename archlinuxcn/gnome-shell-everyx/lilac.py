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
            line = (
                'provides=("gnome-shell=$pkgver")\n'
                + 'conflicts=("gnome-shell")\n'
                + line[:-1]
                + ''' (with everyx's patch)"'''
            )

        elif line.startswith("source=("):
            state = "source"
        elif state == "source" and line == ")":
            line = (
                '  "0001-ibus-candidate-popup-support-rime-comment-style.patch"\n'
                + '  "0002-theme-Fix-jagged-edges-on-notification-buttons.patch"\n'
                + line
            )
            state = "out"

        elif line.startswith("b2sums="):
            state = "b2sums"
        elif state == "b2sums" and line.endswith(")"):
            line = line.replace(
                ")",
                "\n        '1603004291b8dee5bfa8e2ae17893f21e88f9ee7151c67d1c5963fcdadc5a3e3b88ea6571979822c71e0fd39066823a6b4aa317ea1e8ac2880861c75a5b69549'"
                + "\n        '5098032e61deeead14a596104df1c54569ec3f6ff6218cd313c40972435f508d099fef49fee7e19d8d2b4f5c43bd51a4f6d9237d4bd3544ec06764af620cdf53'"
                + ")",
            )
            state = "out"

        elif line.startswith("prepare("):
            state = "prepare"
        elif state == "prepare" and line.endswith("}"):
            line = '  git apply -3 "$srcdir"/*.patch\n' + line
            state = "out"

        elif line.startswith("package_gnome-shell()"):
            line = line.replace("package_gnome-shell()", "package()")

        elif line.startswith("package_gnome-shell-docs()"):
            line = "ignore_" + line.replace("_", "-")

        elif "groups=" in line:
            line = ""

        elif "$pkgbase" in line:
            line = line.replace("$pkgbase", "$_pkgbase")

        print(line)


def post_build():
    git_pkgbuild_commit()
