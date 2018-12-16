# Trimmed lilac.py
#!/usr/bin/env python3

from lilaclib import *

#build_prefix = 'multilib'
#pre_build = aur_pre_build

def post_build():
    run_cmd(['git','add','-f','license.html'])
    git_add_files(['PKGBUILD', 'android-sdk.conf', 'android-sdk.csh', 'android-sdk.install', 'android-sdk.sh'])
    git_commit()

#if __name__ == '__main__':
#  single_main(build_prefix)
