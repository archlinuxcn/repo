#!/usr/bin/env python3

from lilaclib import aur_pre_build
from lilaclib import edit_file
from lilaclib import run_cmd

from pathlib import Path

def pre_build():
    aur_pre_build()
    for line in edit_file("PKGBUILD"):
        if line.startswith("replaces="):
            continue
        print(line)

    file_path = Path("vlc.install")
    if file_path.exists():
        file_path.unlink()
