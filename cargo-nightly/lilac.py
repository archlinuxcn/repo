#!/usr/bin/env python3

import os
import glob
import urllib.request
from urllib.parse import urljoin

import tornado.template
import pytoml

from lilaclib import *

manifest = 'https://static.rust-lang.org/dist/channel-rust-nightly.toml'
debug = False

build_prefix = 'extra-x86_64'

def get_latest_version():
  res = urllib.request.urlopen(manifest)
  page = res.read().decode('utf-8')
  toml = pytoml.loads(page)
  version = toml['pkg']['cargo']['version']
  if version.endswith('-nightly'):
    version = version[:-len('-nightly')]
  version_date = toml['date']
  cargo = toml['pkg']['cargo']['target']['x86_64-unknown-linux-gnu']
  return version, version_date, cargo['url'], cargo['hash']

def pre_build():
  version, version_date, url, file_hash = get_latest_version()
  if not debug:
    oldfiles = glob.glob('*.gz') + glob.glob('*.gz.asc')
    for f in oldfiles:
      os.unlink(f)

  loader = tornado.template.Loader('.')
  content = loader.load('PKGBUILD.tmpl').generate(
    version = version,
    pkgver = version + '_' + version_date.replace('-', ''),
    url = url,
    hash = file_hash,
  )
  with open('PKGBUILD', 'wb') as output:
    output.write(content)

def post_build():
  git_add_files(['PKGBUILD'])
  git_commit()

if __name__ == '__main__':
  single_main()
