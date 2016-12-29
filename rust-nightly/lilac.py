#!/usr/bin/env python3

import os
import glob
import tornado.template
import urllib.request
from urllib.parse import urljoin

from pkg_resources import parse_version

from lilaclib import *

debug = False
_version = '1.16.0'
_version_date = '2016-12-23'

STDS = [
  'arm-unknown-linux-gnueabihf',
  'armv7-unknown-linux-gnueabihf',
  'x86_64-unknown-linux-gnu',
  'i686-unknown-linux-gnu',
  'i686-pc-windows-gnu', # need libgcc_s_dw2-1.dll
  'x86_64-pc-windows-gnu',
  'asmjs-unknown-emscripten',
  'wasm32-unknown-emscripten',
]

dist_url = 'https://static.rust-lang.org/dist/index.html'

build_prefix = 'extra-x86_64'

toolchain = {
  'x86_64-pc-windows-gnu': ['mingw-w64-gcc'],
  'i686-pc-windows-gnu': ['mingw-w64-gcc'],
  'i686-unknown-linux-gnu': ['gcc-multilib'],
  'asmjs-unknown-emscripten': ['emsdk', 'emscripten'],
  'wasm32-unknown-emscripten': ['emsdk', 'emscripten'],
}

def get_latest_version():
  if not debug:
    res = urllib.request.urlopen(dist_url)
    page = res.read().decode('utf-8')
    version_date = re.findall(r'(\d{4}-\d{2}-\d{2})/', page)[-1]
    stable = sorted(set(re.findall(r'\d+\.\d+\.\d+', page)), key=parse_version)[-1]
    major, minor, patchlevel = stable.split('.')
    version = '%s.%s.%s' % (major, int(minor) + 2, patchlevel)
    return version, version_date
  else:
    return _version, _version_date

class Std:
  def __init__(self, platform, date):
    self.name = 'rust-std-nightly-' + platform
    self.url = urljoin(dist_url, date + '/' + self.name + '.tar.gz')
    self.platform = platform
    self.optdepends = toolchain.get(platform)

def pre_build():
  version, version_date = get_latest_version()
  if not debug:
    oldfiles = glob.glob('*.gz') + glob.glob('*.gz.asc')
    for f in oldfiles:
      os.unlink(f)

  stds = [Std(x, version_date) for x in STDS]

  loader = tornado.template.Loader('.')
  content = loader.load('PKGBUILD.tmpl').generate(
    stds = stds,
    version = version,
    version_date = version_date.replace('-', ''),
    version_date_raw = version_date,
  )
  with open('PKGBUILD', 'wb') as output:
    output.write(content)

def post_build():
  git_add_files(['PKGBUILD'])
  git_commit()

if __name__ == '__main__':
  single_main()
