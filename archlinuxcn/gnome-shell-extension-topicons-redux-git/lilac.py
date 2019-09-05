#!/usr/bin/env python3

from lilaclib import *

def post_build():
    aur_post_build()
    update_aur_repo()

