#!/usr/bin/python3

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=["moetayuko", "q234rty"])
    add_replaces(["hyprland-nvidia-hidpi-git"])
    add_depends(["hyprgraphics-git"])

    for line in edit_file("PKGBUILD"):
        print(line.replace("hyprcursor", "hyprcursor-git"))
