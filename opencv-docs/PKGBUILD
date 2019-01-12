# Maintainer:xgdgsc<xgdgsc at gmail dot com>
# Contributor R:ay Rashif <schiv@archlinux.org>
# Contributor: Tobias Powalowski <tpowa@archlinux.org>

#pkgbase=opencv
pkgname=opencv-docs
_realname=opencv
pkgver=4.0.1
pkgrel=1
pkgdesc="Open Source Computer Vision Library docs"
arch=('any')
license=('BSD')
url="http://opencv.org/"

source=("http://downloads.sourceforge.net/opencvlibrary/$pkgver/$_realname-$pkgver-docs.zip")
md5sums=('36c14f195c84336b5c94373c309d4b2a')

build() {
  cd "$srcdir/$pkgver"
}

package() {
  cd "$srcdir/$pkgver"
  mkdir -p "$pkgdir/usr/share/doc/opencv/html"
  cp -r * "$pkgdir/usr/share/doc/opencv/html/"
}

# vim:set ts=2 sw=2 et:
