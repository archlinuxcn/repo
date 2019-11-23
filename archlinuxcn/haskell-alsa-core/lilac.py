from lilaclib import *

def pre_build():
    aur_pre_build()
    add_into_array("depends", ["alsa-lib"])
    add_into_array("makedepends", ["alsa-lib"])

def post_build():
    aur_post_build()

