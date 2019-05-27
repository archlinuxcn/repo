#!/usr/bin/python3

from lilaclib import *

def pre_build():
    aur_pre_build()
    major,minor = "", ""
    for line in edit_file('PKGBUILD'):
        if line.strip().startswith('_subarch='):
            print('_subarch=26')
        elif line.strip().startswith('prepare() {'):
            print('prepare() {')
            print(' _real_prepare | head -n10000000') # limit package() output to 10,000,000 lines
            print('}')
            print('_real_prepare() {')
        elif line.strip().startswith('_major='):
            major = line[len('_major='):].strip()
            print(line)
        elif line.strip().startswith('_minor='):
            minor = line[len('_minor='):].strip()
            print(line)
        elif line.strip().startswith('pkgver='):
            # evaluate and replace pkgver= variable
            print(f"pkgver={major}.{minor}")
        elif line.strip() == "### Compress modules":
            print('    ### Disable modle sig force')
            print('	    sed -i "s|CONFIG_MODULE_SIG_FORCE=y|CONFIG_MODULE_SIG_FORCE=n|g" ./.config ')
            print(line)
        else:
            print(line)


if __name__== '__main__':
    single_main('extra-x86_64')
