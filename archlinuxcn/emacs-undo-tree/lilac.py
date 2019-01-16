# Trimmed lilac.py
#!/usr/bin/env python3

from lilaclib import *

#build_prefix = 'archlinuxcn-x86_64'
#post_build = aur_post_build

def pre_build():
    aur_pre_build()
    for line in edit_file('PKGBUILD'):
        if line.strip().startswith("depends"):
            line += "\nmakedepends=('git')"
        print(line)
    git_add_files('PKGBUILD')
    git_commit()


#if __name__ == '__main__':
#    single_main(build_prefix)
