from lilaclib import aur_pre_build, aur_post_build, add_makedepends

def pre_build():
    aur_pre_build()
    # wget for ./bootstrap and doxygen/pandoc for building docs
    add_makedepends(['wget', 'doxygen', 'pandoc'])

def post_build():
    aur_post_build()
