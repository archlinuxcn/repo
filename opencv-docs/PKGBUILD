# Maintainer:xgdgsc<xgdgsc at gmail dot com>
# Contributor R:ay Rashif <schiv@archlinux.org>
# Contributor: Tobias Powalowski <tpowa@archlinux.org>

#pkgbase=opencv
pkgname=opencv-docs
_realname=opencv
pkgver=3.1.0
pkgrel=1
pkgdesc="Open Source Computer Vision Library docs"
arch=('any')
license=('BSD')
url="http://opencv.org/"
depends=('')
#makedepends=('cmake'  'python2-sphinx' 'texlive-bin' 'texlive-latexextra' 'texlive-fontsextra')
makedepends=('cmake' 'python2-numpy' 'doxygen')

source=("http://downloads.sourceforge.net/opencvlibrary/opencv-unix/$pkgver/$_realname-$pkgver.zip")
md5sums=('6082ee2124d4066581a7386972bfd52a')

_cmakeopts=(
            '-D BUILD_DOCS=ON'
            '-D CMAKE_BUILD_TYPE=Release'
            '-D CMAKE_INSTALL_PREFIX=/usr')

build() {
  cd "$srcdir/$_realname-$pkgver"
  sed -i 's/sphinx-build/sphinx-build2/' cmake/OpenCVDetectPython.cmake
  cmake ${_cmakeopts[@]} .
 # sed -i "s/sphinx-build/sphinx-build2/g" $srcdir/$_realname-$pkgver/doc/CMakeFiles/html_docs.dir/build.make
  #sed -i "s/sphinx-build/sphinx-build2/g" $srcdir/$_realname-$pkgver/doc/CMakeFiles/docs.dir/build.make
  make doxygen
}

package() {
  cd "$srcdir/$_realname-$pkgver"
  mkdir -p "$pkgdir/usr/share/doc/opencv/html"

  cp -r doc/doxygen/html/* "$pkgdir/usr/share/doc/opencv/html/"
  #cp  "$srcdir/$_realname-$pkgver"/doc/*.pdf "$pkgdir/usr/share/doc/opencv/"

}

# vim:set ts=2 sw=2 et:
