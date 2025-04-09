#!/usr/bin/env python3

from lilaclib import aur_pre_build
from lilaclib import edit_file


def pre_build():
    aur_pre_build()
    for line in edit_file("PKGBUILD"):
        if "qt6-quickcontrols2" in line:
            line = line.replace("qt6-quickcontrols2", "qt6-declarative", 1)
        print(line)
