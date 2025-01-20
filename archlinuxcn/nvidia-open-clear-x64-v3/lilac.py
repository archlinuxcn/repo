#!/usr/bin/env python3

import re

from lilaclib import edit_file
from lilaclib import update_pkgver_and_pkgrel
from lilaclib import git_pkgbuild_commit


def pre_build():
    depends_clear_re = re.compile(
        r'''^(\s*depends\+=.*?)['"]?linux-clear-x64-v3[^'") ]*['"]?'''
    )
    kernel = _G.newvers[1]
    update_pkgver_and_pkgrel(_G.newver)
    for line in edit_file('PKGBUILD'):
        m = depends_clear_re.match(line)
        if m:
            line = depends_clear_re.sub(
                r'\1"linux-clear-x64-v3=%s"' % kernel, line
            )
        print(line)

def post_build():
    git_pkgbuild_commit()
