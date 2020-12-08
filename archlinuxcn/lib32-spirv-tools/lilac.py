#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build()
    pattern = re.compile("^ *['\"]?(?:vulkan-tools|spirv-tools)['\"]?$")
    for line in edit_file('PKGBUILD'):
        if not pattern.match(line) and not line.startswith('groups='):
            print(line)

def post_build():
    aur_post_build()
