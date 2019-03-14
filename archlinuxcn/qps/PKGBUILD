# $Id: PKGBUILD 266875 2017-11-15 14:29:11Z foutrelis $
# Maintainer: Sergej Pupykin <pupykin.s+arch@gmail.com>
# Contributor: David Rosenstrauch <darose@darose.net>

pkgname=qps
pkgver=1.10.20
pkgrel=1
pkgdesc="a visual process manager, an X11 version of 'top' or 'ps'."
url="https://github.com/lxqt/qps"
depends=('qt5-x11extras' 'qt5-tools')
makedepends=('cmake' 'lxqt-build-tools>=0.6.0')
arch=('i686' 'x86_64')
license=("GPL")
source=("$pkgname-$pkgver.tar.xz::https://github.com/QtDesktop/qps/releases/download/$pkgver/$pkgname-$pkgver.tar.xz"
	"qps.desktop")
sha256sums=('1570e1cdc95af392ec86a19c29f5bcab784f4913ac1ac57cab398bd759cce737'
            '5216455ce5ce096b36f1b301325fd44c972ff796aa3b40b60807a06dae0ab3f9')

build() {
  mkdir -p build
  cd build
  cmake "$srcdir/$pkgname-$pkgver" \
		-DCMAKE_INSTALL_PREFIX=/usr
  make
}

package() {
	cd build
	make DESTDIR="$pkgdir" install
}
