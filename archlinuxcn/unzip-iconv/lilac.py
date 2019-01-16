#!/usr/bin/env python3
from lilaclib import *

update_on = [{'archpkg': 'unzip'}]
build_prefix = 'extra-x86_64'

def pre_build():
    download_official_pkgbuild('unzip')

    for line in edit_file('PKGBUILD'):
        if 'pkgname=unzip' in line:
            print('pkgname=unzip-iconv')
            print('_'+line)
        elif 'pkgdesc' in line:
            print('pkgdesc="Unpacks .zip archives such as those made by PKZIP. With iconv patch for -O / -I goodness."')
        elif 'depends=' in line:
            print('provides=(\'unzip\')')
            print('conflicts=(\'unzip\')')
        elif 'source=' in line:
            print(line.replace("${pkgname}","$_pkgname"))
            print('        \'unzip60-alt-iconv-utf8.patch\'')
        elif '${pkgname}' in line:
            print(line.replace("${pkgname}","$_pkgname"))
        elif 'sha1sums=' in line:
            print(line)
            print("          '7cb046b09becd96a3901b8ac35f77741695c4a8a'")
        elif 'patch -i ../crc32.patch' in line:
            print(line)
            print('\tpatch -Np1 -i "${srcdir}"/unzip60-alt-iconv-utf8.patch')
        else:
            print(line)

def post_build():
    git_add_files('PKGBUILD')
    git_add_files('unzip60-alt-iconv-utf8.patch')
    git_commit()

if __name__ == '__main__':
    single_main(build_prefix)
