#!/usr/bin/python3
def pre_build():
    _release_tag = _G.newver

    for line in edit_file("PKGBUILD"):
        if line.startswith("_release_tag="):
            line = f"_release_tag={_release_tag}"
        print(line)

    pkgver = _release_tag.lstrip("v").replace("-", "_").lower()
    update_pkgver_and_pkgrel(pkgver)
