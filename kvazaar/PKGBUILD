# Maintainer: Daniel Bermond < yahoo-com: danielbermond >

pkgname=kvazaar
pkgver=0.8.3
pkgrel=1
pkgdesc="An open-source HEVC encoder licensed under LGPLv2.1"
arch=('i686' 'x86_64')
url="http://ultravideo.cs.tut.fi/#encoder"
license=('LGPL2.1')
depends=('glibc')
makedepends=('yasm')
provides=('kvazaar' 'libkvazaar.so')
conflicts=('kvazaar-git')
source=("$pkgname"-"$pkgver".tar.gz::"https://github.com/ultravideo/kvazaar/archive/v${pkgver}.tar.gz")
sha256sums=('a5cebc313bc2edcf631684e67c33227e56d803bfbc940cf8c2f3906b4f543a12')

prepare() {
	cd "$pkgname"-"$pkgver"
	./autogen.sh
}

build() {
	cd "$pkgname"-"$pkgver"
	./configure \
                --prefix=/usr \
                --enable-static=no \
                --enable-shared=yes \
                --enable-fast-install=yes
}

package() {
	cd "$pkgname"-"$pkgver"
	make DESTDIR="$pkgdir/" install
}
