# Maintainer: X0rg

_realname=CPU-X
pkgname=cpu-x
pkgver=4.1.0
pkgrel=1
pkgdesc="A Free software that gathers information on CPU, motherboard and more"
arch=('i686' 'x86_64')
url="http://X0rg.github.io/CPU-X/"
license=('GPL3')
depends=('gtk3' 'ncurses' 'libcpuid' 'pciutils' 'procps-ng')
makedepends=('cmake' 'ninja' 'nasm')
source=("$pkgname-$pkgver.tar.gz::https://github.com/X0rg/CPU-X/archive/v$pkgver.tar.gz")
sha512sums=('4a271b5d62c4c1e1ada5829537517a516d71b43a2202502097e16ca3d1acfaa3f482c71ff4955f429ec75bf88cdb5e1db966c1bbcdcbc7fe925fc23792a76a4b')

build() {
	cmake -S "$_realname-$pkgver" -B build -GNinja -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr
	cmake --build build
}

package() {
	DESTDIR="$pkgdir" ninja -C build install
}
