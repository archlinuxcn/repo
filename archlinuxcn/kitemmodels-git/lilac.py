#!/usr/bin/python

def pre_build():
    for line in edit_file('PKGBUILD'):
        if line.startswith('makedepends'):
            print line.replace("sip4", "sip")
        print(line)
