#!/usr/bin/env python3
from lilaclib import *


def pre_build():
    aur_pre_build(maintainers=["exu", "ruahcra", "Insprill"])

    for line in edit_file("PKGBUILD"):
        print(line)
