#!/usr/bin/env python3

import os
import glob
import tornado.template
import urllib.request
from urllib.parse import urljoin

from pkg_resources import parse_version

from lilaclib import *

debug = False
_version_date = '2016-12-23'

STDS = [
]

dist_url = 'https://static.rust-lang.org/cargo-dist/index.html'

build_prefix = 'extra-x86_64'

toolchain = {
}

def get_latest_version():
  if not debug:
    res = urllib.request.urlopen(dist_url)
    page = res.read().decode('utf-8')
    version_date = re.findall(r'(\d{4}-\d{2}-\d{2})/', page)[-1]
    return version_date
  else:
    return _version_date

class Std:
  def __init__(self, platform, date):
    self.name = 'cargo-nightly-' + platform
    self.url = urljoin(dist_url, date + '/' + self.name + '.tar.gz')
    self.platform = platform
    self.optdepends = toolchain.get(platform)

def pre_build():
  version_date = get_latest_version()
  oldfiles = glob.glob('*.gz') + glob.glob('*.gz.asc')
  for f in oldfiles:
    if not debug:
      os.unlink(f)

  stds = [Std(x, version_date) for x in STDS]

  loader = tornado.template.Loader('.')
  content = loader.load('PKGBUILD.tmpl').generate(
    stds = stds,
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
