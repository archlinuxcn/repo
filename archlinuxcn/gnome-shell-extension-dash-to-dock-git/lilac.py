# Trimmed lilac.py
#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build()
    # for line in edit_file('PKGBUILD'):
    #     if line.startswith('_giturl='):
    #         print('_giturl="git+https://github.com/micheleg/dash-to-dock/#branch=gnome-3-36"')
    #     else:
    #         print(line)

#if __name__ == '__main__':
#    single_main(build_prefix)
