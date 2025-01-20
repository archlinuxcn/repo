#!/usr/bin/env python3

import re

from lilaclib import edit_file


def pre_build():
    depends_clear_re = re.compile(
        r'''^(\s*depends\+=.*?)['"]?linux-clear-x64-v3[^'") ]*['"]?'''
    )
    kernel = _G.newvers[1]
    for line in edit_file('PKGBUILD'):
        m = depends_clear_re.match(line)
        if m:
            line = depends_clear_re.sub(
                r'\1"linux-clear-x64-v3=%s"' % kernel, line
            )
        print(line)
