#!/usr/bin/env python3

from lilaclib import *
import re
import urllib.request

def pre_build():
  # Upstream tags look like v02.09.01.70 (the `v` is stripped by the
  # `prefix` option in lilac.yaml). The tag (without `v`) is used verbatim
  # for the source URL, and pkgver is the same with leading zeros removed.
  raw_ver = _G.newver
  if not re.fullmatch(r'[0-9]+(\.[0-9]+)+', raw_ver):
    raise ValueError(f'unexpected version format: {raw_ver!r}')
  pkgver = '.'.join(str(int(part)) for part in raw_ver.split('.'))

  # OpenMeshCraft is built from the commit pinned by the release
  url = ('https://raw.githubusercontent.com/bambulab/BambuStudio/'
         f'v{raw_ver}/deps/OpenMeshCraft/OpenMeshCraft.cmake')
  with urllib.request.urlopen(url) as res:
    recipe = res.read().decode()
  m = re.search(r'OpenMeshCraft/archive/([0-9a-f]{40})\.zip', recipe)
  if not m:
    raise ValueError('cannot find the OpenMeshCraft commit in the recipe')
  omc_commit = m.group(1)

  for line in edit_file('PKGBUILD'):
    if line.startswith('_raw_pkgver='):
      line = f'_raw_pkgver={raw_ver}'
    elif line.startswith('_omc_commit='):
      line = f'_omc_commit={omc_commit}'
    print(line)

  # Updates pkgver, resets pkgrel and runs updpkgsums
  update_pkgver_and_pkgrel(pkgver, updpkgsums=True)
