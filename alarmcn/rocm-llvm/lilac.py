#!/usr/bin/env python3

from types import SimpleNamespace

from lilaclib import *

g = SimpleNamespace()

patch_str = """
source+=(https://github.com/llvm/llvm-project/commit/078c18de832328f743fb6e8dce728a030c81dc0d.patch)
prepare() {
  cd rocm-llvm

  patch -Np1 --no-backup-if-mismatch < "../078c18de832328f743fb6e8dce728a030c81dc0d.patch"
}
"""

def pre_build():
  g.files = download_official_pkgbuild('rocm-llvm')

  for line in edit_file('PKGBUILD'):
    line = line.replace('AMDGPU;NVPTX;X86', 'AMDGPU;NVPTX;AArch64')
    if line.startswith('arch='):
      line = 'arch=(aarch64)'
    if line.startswith('build()'):
      print(patch_str)
    print(line)
  run_cmd(['updpkgsums'])

def post_build():
  git_add_files([f for f in g.files if not f.startswith(".")])
  git_commit()
