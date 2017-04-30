#!/usr/bin/env python3

from lilaclib import *

build_prefix = 'extra-x86_64'

def pre_build():
  aur_pre_build()

  for line in edit_file('PKGBUILD'):
    if 'MOZ_REQUIRE_SIGNING' in line:
      continue
    if line.strip() == 'cd firefox-${pkgver}esr':
      line += "\nsed -i '3abuild = false' media/libstagefright/binding/mp4parse_capi/Cargo.toml"
    print(line)

post_build = aur_post_build

if __name__ == '__main__':
  single_main()
