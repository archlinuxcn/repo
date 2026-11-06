#!/usr/bin/env python3

from lilaclib import *
import re
import urllib.request

def pre_build():
  pkgver = _G.newver
  if not re.fullmatch(r'[0-9]+(\.[0-9]+)+', pkgver):
    raise ValueError(f'unexpected version format: {pkgver!r}')

  # bambu-studio version with only the first three components (e.g. 2.9.1),
  # already trimmed by the from_pattern/to_pattern of update_on_build.
  studio_ver = _G.on_build_vers[0][1] if _G.on_build_vers else ''
  if not studio_ver:
    # No build database, fall back to the packaged bambu-studio version
    with open('../bambu-studio/PKGBUILD') as f:
      m = re.search(r'^pkgver=([0-9]+\.[0-9]+\.[0-9]+)\.', f.read(), re.M)
    studio_ver = m.group(1) if m else ''
  if not re.fullmatch(r'[0-9]+\.[0-9]+\.[0-9]+', studio_ver or ''):
    raise ValueError(f'unexpected bambu-studio version format: {studio_ver!r}')
  studio_abi = '.'.join(f'{int(part):02d}' for part in studio_ver.split('.'))

  # The vendored mosquitto has to match the tag pinned by the release
  url = f'https://raw.githubusercontent.com/ClusterM/open-bamboo-networking/v{pkgver}/CMakeLists.txt'
  with urllib.request.urlopen(url) as res:
    cmake = res.read().decode()
  m = re.search(r'^set\(OBN_MOSQUITTO_GIT_TAG "v([^"]+)"', cmake, re.M)
  if not m:
    raise ValueError('cannot find the mosquitto version in CMakeLists.txt')
  mosquitto_ver = m.group(1)

  for line in edit_file('PKGBUILD'):
    if line.startswith('_studio_abi='):
      line = f'_studio_abi={studio_abi}'
    elif line.startswith('_mosquitto_ver='):
      line = f'_mosquitto_ver={mosquitto_ver}'
    print(line)

  update_pkgver_and_pkgrel(pkgver, updpkgsums=True)
