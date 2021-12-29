#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *

def pre_build():
    aur_pre_build(maintainers=['alerque','farseerfc','yar','hcsch'])
    add_makedepends(['rustup']) 

if __name__ == '__main__':
    single_main()
