#!/usr/bin/env python3

from lilaclib import *
from pyalpm import vercmp

prefix = 'refs/tags/archcn-'

def _get_new_version(major):
  ver_prefix = f'{prefix}{major}.'
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
  if _G.newver != _G.newvers[1]:
    raise ValueError('Upstream LLVM version mismatch, manual update required.')
  archcn_ver_commit = _G.newvers[4]
  if _G.newvers[1] != _G.newvers[2]:
    archcn_ver = _get_new_version(_G.newvers[1])
    if archcn_ver:
      raise ValueError('New tagged release available.')
    versioned_llvm = _G.newvers[2]
  else:
    versioned_llvm = ''
  archcn_ver = _get_new_version(_G.newvers[2])
  if archcn_ver_commit != '0':
    if archcn_ver:
      raise ValueError('New tagged release available.')
    pkgver, archcn_commit = archcn_ver_commit.split('-', 2)
    for line in edit_file('PKGBUILD'):
      if line.startswith('_archcn_rel='):
        line = f'_archcn_rel='
      if line.startswith('_archcn_commit='):
        line = f'_archcn_commit={archcn_commit}'
      if line.startswith('_versioned_llvm='):
        line = f'_versioned_llvm={versioned_llvm}'
      print(line)
  else:
    if not archcn_ver:
      raise ValueError('Cannot find new version')
    pkgver, archcn_rel = archcn_ver.split('-', 2)
    for line in edit_file('PKGBUILD'):
      if line.startswith('_archcn_rel='):
        line = f'_archcn_rel={archcn_rel}'
      if line.startswith('_archcn_commit='):
        line = f'_archcn_commit='
      if line.startswith('_versioned_llvm='):
        line = f'_versioned_llvm={versioned_llvm}'
      print(line)
  update_pkgver_and_pkgrel(pkgver)
