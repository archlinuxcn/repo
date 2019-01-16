#!/usr/bin/env python3
from lilaclib import *

update_on = [{'aur': 'js-beautify'}]
build_prefix = 'extra-x86_64'

def pre_build():
    aur_pre_build('js-beautify')

    for line in edit_file('PKGBUILD'):
        if 'pkgname=' in line:
            print(line.replace('js-beautify','js-beautify-archlinuxcn'))
        elif 'conflicts=' in line:
            print('provides=("js-beautify")')
            print('conflicts=("js-beautify")')
        elif 'npm install' in line:
            print(line)
            print('  cd $pkgdir/usr/bin;for i in *;do mv $i node-$i;done')
        else:
            print(line)

post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)
