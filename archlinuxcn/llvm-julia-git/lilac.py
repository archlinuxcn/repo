#!/usr/bin/env python3

from lilaclib import *
from pyalpm import vercmp

prefix = 'refs/tags/archcn-'

def _get_new_version(upstream_ver):
  ver_prefix = f'{prefix}{upstream_ver}-'
  tags = s.get("https://api.github.com/repos/yuyichao/llvm-project/git/refs/tags").json()
  max_ver = ''
  for tag in tags:
    if not tag.get('ref', '').startswith(ver_prefix):
      continue
    ver = tag['ref'].removeprefix(prefix)
    if not max_ver or vercmp(ver, max_ver):
      max_ver = ver
  return max_ver

def pre_build():
  upstream_ver = _G.newver
  archcn_ver = _get_new_version(upstream_ver)
  if not archcn_ver:
    raise ValueError(f'Cannot find archcn tag for {upstream_ver}')
  pkgver, archcn_rel = archcn_ver.split('-', 2)
  for line in edit_file('PKGBUILD'):
    if line.startswith('_archcn_rel='):
      line = f'_archcn_rel={archcn_rel}'
    if line.startswith('_archcn_commit='):
      line = f'_archcn_commit='
    if line.startswith('_versioned_llvm='):
      line = f'_versioned_llvm='
    print(line)
  update_pkgver_and_pkgrel(pkgver)
