# Maintainer: X0rg

_realname=CPU-X
pkgname=cpu-x
pkgver=4.3.1
pkgrel=1
pkgdesc="A Free software that gathers information on CPU, motherboard and more"
arch=('i686' 'x86_64')
url="http://X0rg.github.io/CPU-X/"
license=('GPL3')
depends=('gtk3' 'ncurses' 'libcpuid' 'pciutils' 'glfw' 'opencl-icd-loader' 'procps-ng')
makedepends=('cmake' 'ninja' 'nasm' 'opencl-headers')
optdepends=('opencl-driver: packaged opencl driver')
source=("$pkgname-$pkgver.tar.gz::https://github.com/X0rg/CPU-X/archive/v$pkgver.tar.gz")
sha512sums=('43e7bc4b82a15545e4c2f69f598a94706ef2c5f5594ff50763f71722d1b98e6dd56e907a4f35917500debf11522c5908dbebf51f515fe5a51af7282254210bc1')

build() {
	cmake -S "$_realname-$pkgver" -B build -GNinja -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_INSTALL_LIBEXECDIR="lib/cpu-x"
	cmake --build build
}

package() {
	DESTDIR="$pkgdir" cmake --install build
}
