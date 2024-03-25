#!/usr/bin/env python3

from lilaclib import aur_pre_build
from lilaclib import run_cmd
from lilaclib import edit_file


def pre_build():
    aur_pre_build()
    run_cmd(["iconv", "-f", "iso-8859-1", "-t", "utf-8", "PKGBUILD", "-o", "PKGBUILD"])
    for line in edit_file("PKGBUILD"):
        if "tm@t8m.info" in line:
            line = (
                line[: line.find("#")] + "# Tomas Mraz <tm@t8m.info>"
            )  # sorry Tomas Mraz, your name is just corrupted UTF-8
        print(line)
