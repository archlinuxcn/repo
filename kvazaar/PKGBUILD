# Maintainer: Daniel Bermond < yahoo-com: danielbermond >

pkgname=kvazaar
pkgver=1.0.0
pkgrel=4
pkgdesc="An open-source HEVC encoder licensed under LGPLv2.1"
arch=('i686' 'x86_64')
url="http://ultravideo.cs.tut.fi/#encoder"
license=('LGPL2.1')
depends=('glibc' 'crypto++')
makedepends=('yasm')
provides=('libkvazaar.so')
conflicts=('kvazaar-git')
source=("$pkgname"-"$pkgver".tar.gz::"https://github.com/ultravideo/kvazaar/archive/v${pkgver}.tar.gz"
        "cryptopp-fix.patch"::"https://github.com/ultravideo/kvazaar/commit/8ae791a3e13c592f3efe695bafe366f66a376498.diff")
sha256sums=('40eb7b4b23897299e99050f0c011e9380cf898b25615dd143f018b278b972a46'
            '79c8a9f7ca41c5c5b197888082700c5b7ee8e7d07888a6162fc4276ea0c40111')

prepare() {
	cd "$pkgname"-"$pkgver"
	
	patch -Np1 -i ../cryptopp-fix.patch
	./autogen.sh
}

build() {
	cd "$pkgname"-"$pkgver"
	
	./configure \
                --prefix=/usr \
                --enable-static=no \
                --enable-shared=yes \
                --enable-fast-install=yes \
                --with-cryptopp
}

package() {
	cd "$pkgname"-"$pkgver"
	make DESTDIR="$pkgdir/" install
}
