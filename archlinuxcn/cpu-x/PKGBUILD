# Maintainer: X0rg

_realname=CPU-X
pkgname=cpu-x
pkgver=4.0.1
pkgrel=1
pkgdesc="A Free software that gathers information on CPU, motherboard and more"
arch=('i686' 'x86_64')
url="http://X0rg.github.io/CPU-X/"
license=('GPL3')
depends=('gtk3' 'ncurses' 'libcpuid' 'pciutils' 'procps-ng')
makedepends=('cmake' 'ninja' 'nasm')
source=("$pkgname-$pkgver.tar.gz::https://github.com/X0rg/CPU-X/archive/v$pkgver.tar.gz")
sha512sums=('44bdc21ab73eb16f54a354870cd1552dc7c98030264f21cd17d20550e83d6e446d65de9398242a2d107e9213ce66a6a1d855918447abdd9ae81c6e54d25e4243')

build() {
	cmake -S "$_realname-$pkgver" -B build -GNinja -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr
	cmake --build build
}

package() {
	DESTDIR="$pkgdir" ninja -C build install
}
