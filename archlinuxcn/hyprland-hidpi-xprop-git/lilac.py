#!/usr/bin/python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=["moetayuko", "q234rty"])
    add_replaces(["hyprland-nvidia-hidpi-git"])

    for line in edit_file("PKGBUILD"):
        print(
            line.replace("aquamarine", "aquamarine-git")
            .replace("hyprcursor", "hyprcursor-git")
            .replace("hyprlang", "hyprlang-git")
        )
