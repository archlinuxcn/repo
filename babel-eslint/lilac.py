# Trimmed lilac.py
#!/usr/bin/env python3

from lilaclib import *

#build_prefix = 'extra-x86_64'

def pre_build():
  oldver = _G.oldver
  ver = _G.newver
  need_update_pkgrel = False

  for line in edit_file('PKGBUILD'):
    if line.startswith('pkgver='):
      print('pkgver=%s' % ver)
      continue
    elif line.startswith('pkgrel='):
      if oldver == ver:
        need_update_pkgrel = True
        print(line)
      else:
        print('pkgrel=1')
      continue

    print(line)

  if need_update_pkgrel:
    update_pkgrel()

  run_cmd(['updpkgsums'])

def post_build():
  git_add_files(['PKGBUILD'])
  git_commit()

#if __name__ == '__main__':
#  single_main(build_prefix)

