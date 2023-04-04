#!/usr/bin/python3

from lilaclib import *

def pre_build():
    aur_pre_build(name='sysmontask', maintainers=['yochananmarqos','camel-neeraj'])

    for line in edit_file('PKGBUILD'):
        if line.startswith('pkgname='):
            print ('pkgname=sysmontask-git')
        else:
            print (line.replace('$pkgname','sysmontask'))
