#!/usr/bin/env python3

import re

from lilaclib import edit_file
from lilaclib import update_pkgver_and_pkgrel
from lilaclib import git_pkgbuild_commit


def pre_build():
    depends_kernel_re = re.compile(
        r'''^(\s*depends\+=.*?)['"]?\$\{_lkname\}[^'") ]*['"]?'''
    )
    kernver = _G.newvers[1]
    update_pkgver_and_pkgrel(_G.newver, updpkgsums=False)
    for line in edit_file('PKGBUILD'):
        m = depends_kernel_re.match(line)
        if m:
            line = depends_kernel_re.sub(
                r'\1"${_lkname}=%s"' % kernver, line
            )
        print(line)


def post_build():
    git_pkgbuild_commit()
