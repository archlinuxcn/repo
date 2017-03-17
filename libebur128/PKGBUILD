# $Id$
# Maintainer: BoosterDEV <booster DOT devel AT gmail DOT com>

pkgname=libebur128
pkgver=1.2.2
pkgrel=1
pkgdesc="A library that implements the EBU R 128 standard for loudness normalisation."
arch=('i686' 'x86_64')
url="https://github.com/jiixyj/libebur128"
license=('MIT')
depends=('speex')
makedepends=('cmake')
source=(
	"$pkgname-$pkgver.tar.gz::https://github.com/jiixyj/$pkgname/archive/v$pkgver.tar.gz"
)
sha256sums=('1d0d7e855da04010a2432e11fbc596502caf11b61c3b571ccbcb10095fe44b43')

prepare() {
	cd "$pkgname-$pkgver"

	[[ -d build ]] && rm -rf build
	mkdir build
}

build() {
	cd "$pkgname-$pkgver"

	cd build
	cmake .. \
		-DCMAKE_BUILD_TYPE=Release \
		-DCMAKE_INSTALL_PREFIX=/usr \
        -DCMAKE_INSTALL_LIBDIR=lib
	make
}

package() {
	cd "$pkgname-$pkgver"

	cd build
	make DESTDIR="$pkgdir" install
}
