#!/usr/bin/python3

from lilaclib import *

def pre_build():
    aur_pre_build(name='sysmontask', maintainers=['yochananmarqos','camel-neeraj'])

    for line in edit_file('PKGBUILD'):
        if line.strip().startswith('pkgname='):
            print ('pkgname=sysmontask-git')
        elif line.strip().startswith('git describe'):
            print ('git describe --long --tags --exclude v1.x.x | sed \'s/\\([^-]*-g\\)/r\\1/;s/-/./g;s/v//\'')
        elif line.strip().startswith('epoch='):
            print ('epoch=2')
        else:
            print (line.replace('$pkgname','sysmontask'))
