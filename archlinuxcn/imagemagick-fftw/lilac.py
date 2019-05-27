from types import SimpleNamespace

from lilaclib import *

g = SimpleNamespace()

def pre_build():
  g.oldfiles = clean_directory()
  g.files = download_official_pkgbuild('imagemagick')

  makedepends = False
  packaging_imagemagick = False
  for line in edit_file('PKGBUILD'):
    if line.startswith('pkgbase='):
      line = 'pkgbase=imagemagick-fftw'
    elif line.startswith('pkgname='):
      line = 'pkgname=(imagemagick-fftw)'
    elif line.startswith('makedepends=('):
      makedepends = True
    elif makedepends and line.endswith(')'):
      line = line.replace(')', " 'fftw')")
      makedepends = False
    elif '--without-fftw' in line:
      line = line.replace('--without-fftw', '--with-fftw')
    elif line.startswith('package_imagemagick('):
      packaging_imagemagick = True
      line = 'package_imagemagick-fftw() {'
    elif packaging_imagemagick and 'conflicts=' in line:
      line = '  conflicts=(imagemagick6 imagemagick)'
    elif packaging_imagemagick and 'provides=' in line:
      line = '  provides=(libmagick libmagick-fftw imagemagick=$pkgver)'
    elif packaging_imagemagick and 'replaces=' in line:
      line = '  replaces=(libmagick-fftw)'
    elif packaging_imagemagick and line == '}':
      packaging_imagemagick = False
    elif line.startswith('package_imagemagick-doc('):
      break
    print(line)

def post_build():
  git_rm_files(g.oldfiles)
  git_add_files(g.files)
  git_commit()
  update_aur_repo()
