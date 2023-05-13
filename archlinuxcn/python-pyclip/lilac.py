#!/usr/bin/python3

def pre_build():
    aur_pre_build(maintainers=['ImperatorStorm'])

    for line in edit_file('PKGBUILD'):
        if not line.strip().startswith('depends=(python-argparse'):
            print (line)
