# Trimmed lilac.py
#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *

def update_epoch(epoch):
    with open('PKGBUILD') as f:
        pkgbuild = f.read()
    pkgbuild = re.sub(r'''(?<=^epoch=)['"]?([\d]+)['"]?''', epoch, pkgbuild, count=1, flags=re.MULTILINE)
    with open('PKGBUILD', 'w') as f:
        f.write(pkgbuild)
    logger.info('epoch updated to %s', epoch)

def pre_build():
    newver = _G.newver.split(":")[1]
    newepoch = _G.newver.split(":")[0]
    update_pkgver_and_pkgrel(newver)
    update_epoch(newepoch)

def post_build():
    update_aur_repo()
    git_add_files("PKGBUILD")
    git_commit()

#if __name__ == '__main__':
#  single_main()
