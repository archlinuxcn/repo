#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *

build_prefix = 'extra-x86_64'

def pre_build():
    aur_pre_build()
    for line in edit_file('PKGBUILD'):
        print(line)
        if line.strip().startswith("cp -a"):
            print('python2 -m compileall $pkgdir/opt/zeronet')
    for line in edit_file('zeronet.install'):
        if line.strip().startswith("chown -R zeronet:zeronet /opt/zeronet"):
            continue # do not chown /opt/zeronet
        print(line)
    for line in edit_file('zeronet.service'):
        if line.strip().startswith("ExecStart=/usr/bin/env"):
            print("""StandardOutput=null
StandardError=null
PrivateTmp=true
PrivateDevices=true
ProtectSystem=full
ProtectHome=true
NoNewPrivileges=true
CapabilityBoundingSet=""")
            line = "ExecStart=/opt/zeronet/zeronet.py --config_file /etc/zeronet.conf"
        print(line)
    run_cmd("updpkgsums")
    for line in edit_file('PKGBUILD'):
        if line.strip().startswith("pkgrel="):
            line = line.strip()+".1"
        print(line)


post_build = aur_post_build

if __name__ == '__main__':
    single_main(build_prefix)

