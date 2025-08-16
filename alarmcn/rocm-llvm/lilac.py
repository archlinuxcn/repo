#!/usr/bin/env python3

from types import SimpleNamespace

from lilaclib import *

g = SimpleNamespace()

def pre_build():
  g.files = download_official_pkgbuild('rocm-llvm')

  for line in edit_file('PKGBUILD'):
    line = line.replace('AMDGPU;NVPTX;X86', 'AMDGPU;NVPTX;AArch64')
    if line.startswith('arch='):
      line = 'arch=(aarch64)'
    if line.startswith('prepare()'):
      print('source+=(0001-Fix-merge-error-for-ptrauth-support.patch)')
      print("""prepare() {
  (cd rocm-llvm/
  patch -Np1 -i "$srcdir/0001-Fix-merge-error-for-ptrauth-support.patch")
  _prepare
}
""")
      print(f"_{line}")
      continue
    print(line)
  run_cmd(['updpkgsums'])

def post_build():
  git_add_files([f for f in g.files if not f.startswith(".")])
  git_commit()
