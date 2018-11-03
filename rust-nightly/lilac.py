#!/usr/bin/env python3

import os
import glob
import tornado.template

import pytoml

from lilaclib import s, git_add_files, git_commit, single_main

debug = False

STDS = [
  'arm-unknown-linux-gnueabihf',
  'armv7-unknown-linux-gnueabihf',
  'x86_64-unknown-linux-gnu',
  'i686-unknown-linux-gnu',
  'i686-pc-windows-gnu', # need libgcc_s_dw2-1.dll
  'x86_64-pc-windows-gnu',
  'wasm32-unknown-unknown',
  'aarch64-linux-android',
]

config_url = 'https://static.rust-lang.org/dist/channel-rust-nightly.toml'

toolchain = {
  'x86_64-pc-windows-gnu': ['mingw-w64-gcc'],
  'i686-pc-windows-gnu': ['mingw-w64-gcc'],
  'i686-unknown-linux-gnu': [],
  'asmjs-unknown-emscripten': ['emsdk', 'emscripten'],
  'wasm32-unknown-emscripten': ['emsdk', 'emscripten'],
  'wasm32-unknown-unknown': [],
  'aarch64-linux-android': ['android-ndk'],
}

class Std:
  def __init__(self, target, data):
    if not data['available']:
      raise Exception('target not available', target)
    self.name = f'rust-std-nightly-{target}'
    self.url = data['xz_url']
    self.hash = data['xz_hash']
    self.target = target
    self.optdepends = toolchain.get(target)

def pre_build():
  toml = s.get(config_url).text
  toml = pytoml.loads(toml)

  version_date = toml['date']
  version = toml['pkg']['rust']['version'].split('-', 1)[0]
  cargo_version = toml['pkg']['cargo']['version'].split('-', 1)[0]
  rustfmt_version = toml['pkg']['rustfmt-preview']['version'].split('-', 1)[0]
  clippy_version = toml['pkg']['clippy-preview']['version'].split('-', 1)[0]
  clippy_url = toml['pkg']['clippy-preview']['target'] \
      ['x86_64-unknown-linux-gnu']['xz_url']

  if not debug:
    oldfiles = (glob.glob('*.xz') + glob.glob('*.xz.asc') +
                glob.glob('*.part'))
    for f in oldfiles:
      os.unlink(f)

  stds = [Std(target, toml['pkg']['rust-std']['target'][target])
          for target in STDS]

  loader = tornado.template.Loader('.')
  content = loader.load('PKGBUILD.tmpl').generate(
    stds = stds,
    version = version,
    version_date = version_date.replace('-', ''),
    version_date_raw = version_date,
    cargo_version = cargo_version,
    rustfmt_version = rustfmt_version,
    clippy_version = clippy_version,
    clippy_url = clippy_url,
  )
  with open('PKGBUILD', 'wb') as output:
    output.write(content)

def post_build():
  git_add_files(['PKGBUILD'])
  git_commit()

if __name__ == '__main__':
  single_main()
