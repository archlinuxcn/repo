# Trimmed lilac.py
from types import SimpleNamespace

from lilaclib import *

g = SimpleNamespace()

#build_prefix = 'extra-x86_64'

def pre_build():
  g.oldfiles = clean_directory()
  g.files = download_official_pkgbuild('imagemagick')

  makedepends = False
  change_depends = False
  for line in edit_file('PKGBUILD'):
    if line.startswith('pkgbase='):
      line = 'pkgbase=imagemagick-fftw'
    elif line.startswith('pkgname='):
      line = 'pkgname=(libmagick-fftw imagemagick-fftw)'
    elif line.startswith('makedepends=('):
      makedepends = True
    elif makedepends and line.endswith(')'):
      line = line.replace(')', " 'fftw')")
      makedepends = False
    elif '--without-fftw' in line:
      line = line.replace('--without-fftw', '--with-fftw')
    elif line.startswith('package_imagemagick('):
      change_depends = True
      line = 'package_imagemagick-fftw() {'
      line += '\n  provides=("imagemagick=$pkgver")\n'
      line += '  conflicts=("imagemagick")'
    elif line.startswith('package_libmagick('):
      line = 'package_libmagick-fftw() {'
      line += '\n  provides=("libmagick=$pkgver")\n'
      line += '  conflicts=("libmagick")'
    elif change_depends and line.lstrip().startswith('depends='):
      line = line.replace('libmagick', 'libmagick-fftw')
      change_depends = False
    elif line.startswith('package_imagemagick-doc('):
      break
    print(line)

def post_build():
  git_rm_files(g.oldfiles)
  git_add_files(g.files)
  git_commit()
  update_aur_repo()

#if __name__ == '__main__':
#  single_main()
