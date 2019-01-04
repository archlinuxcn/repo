# Trimmed lilac.py
#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *

#build_prefix = 'extra-x86_64'

def pre_build():
  pkgver = run_cmd(['sh', '-c', "git ls-remote --tags https://gitlab.com/vedvyas/doxytag2zealdb.git | sed -n '${s#^.*tags\/v##p}' | sed -n 's/\^{}//p'"]).rstrip()
  run_cmd(['sh', '-c', 'sed -i "/^pkgver/s/^.*$/pkgver=' + pkgver + '/" PKGBUILD'])


def post_build():
  git_add_files('PKGBUILD')
  git_commit()

#if __name__ == '__main__':
#  single_main()
