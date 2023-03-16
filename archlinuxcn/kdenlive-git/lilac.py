#!/usr/bin/python

def pre_build():
    aur_pre_build(maintainers=['evorster'])

    for line in edit_file("PKGBUILD"):
        if not (line.strip().startswith("cp -v")):
            print (line)
