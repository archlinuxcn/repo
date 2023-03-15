#!/usr/bin/python

def pre_build():
    for line in edit_file('PKGBUILD'):
        if not (line.strip().startswith("replaces=('sip")):
            print (line)
