# Maintainer: X0rg

_realname=CPU-X
pkgname=cpu-x
pkgver=4.2.0
pkgrel=1
pkgdesc="A Free software that gathers information on CPU, motherboard and more"
arch=('i686' 'x86_64')
url="http://X0rg.github.io/CPU-X/"
license=('GPL3')
depends=('gtk3' 'ncurses' 'libcpuid' 'pciutils' 'glfw' 'procps-ng')
makedepends=('cmake' 'ninja' 'nasm')
source=("$pkgname-$pkgver.tar.gz::https://github.com/X0rg/CPU-X/archive/v$pkgver.tar.gz")
sha512sums=('28d51ecd1086624310825d83820051e2d97f2cb10b8b4af3aa69c372854331fdd29100fb932972a4a787187f42894ae93ad830c29aaa5a75b2dc72d765ee4b10')

build() {
	cmake -S "$_realname-$pkgver" -B build -GNinja -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr
	cmake --build build
}

package() {
	DESTDIR="$pkgdir" ninja -C build install
}
