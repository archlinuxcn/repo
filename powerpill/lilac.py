# Trimmed lilac.py
#!/usr/bin/env python3
#
# This file is the most simple lilac.py file,
# and it suits for most packages in AUR.
#

from lilaclib import *

#build_prefix = 'extra-x86_64'
depends = ['python3-memoizedb', 'python3-xcgf', 'python3-xcpf', 'pm2ml']

def pre_build():
  # obtain base PKGBUILD, e.g.
  aur_pre_build()

  count=0
  for line in edit_file('PKGBUILD'):
    # edit PKGBUILD
    count=count+1
    if count in {14,18,22,24}:
        print('#'+line)
    else:
        print(line)

#post_build = aur_post_build

#if __name__ == '__main__':
#  single_main()
