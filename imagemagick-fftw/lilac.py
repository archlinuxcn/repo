import fileinput
from types import SimpleNamespace

from lilaclib import *

g = SimpleNamespace()

build_prefix = 'extra-x86_64'

def pre_build():
  g.oldfiles = clean_directory()
  g.files = download_official_pkgbuild('imagemagick')

  with fileinput.input(files=('PKGBUILD',), inplace=True) as f:
    makedepends = False
    packaging = False
    for line in f:
      line = line.rstrip('\n')
      if line.startswith('pkgbase='):
        continue
      elif line.startswith('pkgname='):
        line = 'pkgname=imagemagick-fftw'
      elif line.startswith('makedepends=('):
        makedepends = True
      elif makedepends and line.endswith(')'):
        line = line.replace(')', " 'fftw')")
        makedepends = False
      elif '--without-fftw' in line:
        line = line.replace('--without-fftw', '--with-fftw')
      elif line.startswith('package_imagemagick('):
        line = 'package() {'
        packaging = True
      elif packaging and not line:
        line = '  provides=("imagemagick=$pkgver")\n'
        line += '  conflicts=("imagemagick")'
      elif packaging and line.startswith('}'):
        packaging = False
      elif line.startswith('package_imagemagick-doc('):
        break
      print(line)

def post_build():
  git_rm_files(g.oldfiles)
  git_add_files(g.files)
  git_commit()

if __name__ == '__main__':
  import os
  lilac_build(
    build_prefix = 'makepkg',
    repodir = os.path.dirname(os.path.dirname(__file__))
  )
