#!/usr/bin/env python3

from lilaclib import *
import re

def pre_build():
  # Upstream tags look like v02.09.01.70 (the `v` is stripped by the
  # `prefix` option in lilac.yaml). The tag (without `v`) is used verbatim
  # for the source URL, and pkgver is the same with leading zeros removed.
  raw_ver = _G.newver
  if not re.fullmatch(r'[0-9]+(\.[0-9]+)+', raw_ver):
    raise ValueError(f'unexpected version format: {raw_ver!r}')
  pkgver = '.'.join(str(int(part)) for part in raw_ver.split('.'))

  for line in edit_file('PKGBUILD'):
    if line.startswith('_raw_pkgver='):
      line = f'_raw_pkgver={raw_ver}'
    print(line)

  # Updates pkgver, resets pkgrel and runs updpkgsums
  update_pkgver_and_pkgrel(pkgver, updpkgsums=True)
