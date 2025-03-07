#!/usr/bin/env python3

from lilaclib import aur_pre_build
from lilaclib import edit_file
from lilaclib import run_cmd

def pre_build():
    aur_pre_build()
    in_nvidia_open = False
    for line in edit_file("PKGBUILD"):
        if "_build_nvidia_open:=no" in line:
            line = line.replace(":=no", ":=yes")
        elif line.startswith("_package-nvidia-open()"):
            in_nvidia_open = True
        elif in_nvidia_open and "provides=('NVIDIA-MODULE')" in line:
            line = line.replace("provides=('NVIDIA-MODULE')", "provides=(\"nvidia-open=${pkgver}\")")
            in_nvidia_open = False
        print(line)
    run_cmd(["updpkgsums"])
