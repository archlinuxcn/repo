#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *

build_prefix = 'extra-x86_64'


def pre_build():
    aur_pre_build("firefox-nightly")
    with open("vendor.js","a") as vendor:
        vendor.write('pref("intl.locale.matchOS", true);\n')
    run_cmd(['updpkgsums'])


def post_build():
    # do something after the package has successfully been built
    aur_post_build()


if __name__ == '__main__':
    single_main()
