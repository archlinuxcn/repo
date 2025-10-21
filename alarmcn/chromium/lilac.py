#!/usr/bin/env python3

from types import SimpleNamespace

from lilaclib import *

import shutil

g = SimpleNamespace()

def pre_build():
  g.files = download_official_pkgbuild('chromium')

  # Fix from upstream, can be removed once there's a new archlinux package built
  shutil.copyfile('compiler-rt-adjust-paths.patch.fix',
                  'compiler-rt-adjust-paths.patch')

  with open('fetch-chromium-release', 'a') as io:
    print('\nln -sf /usr/bin/node ../chromium-$VERSION/third_party/node/linux/node-linux-x64/bin/', file=io)

  for line in edit_file('PKGBUILD'):
    if line.startswith('arch='):
      line = 'arch=(aarch64 x86_64)'
    print(line)

  run_protected(["updpkgsums"])

def post_build():
  git_add_files([f for f in g.files if not f.startswith(".")])
  git_commit()
