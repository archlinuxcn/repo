# Maintainer: X0rg

_realname=CPU-X
pkgname=cpu-x
pkgver=4.3.0
pkgrel=1
pkgdesc="A Free software that gathers information on CPU, motherboard and more"
arch=('i686' 'x86_64')
url="http://X0rg.github.io/CPU-X/"
license=('GPL3')
depends=('gtk3' 'ncurses' 'libcpuid' 'pciutils' 'glfw' 'opencl-icd-loader' 'procps-ng')
makedepends=('cmake' 'ninja' 'nasm' 'opencl-headers')
optdepends=('opencl-driver: packaged opencl driver')
source=("$pkgname-$pkgver.tar.gz::https://github.com/X0rg/CPU-X/archive/v$pkgver.tar.gz")
sha512sums=('0edd706dae2ab84e4fa07ea5dc6798132cd6155219acdc20fd32a3a98ca6f17606496a6f578a53b93d5cf2e27f18787ee50329651cf9782d1dedd347818f8811')

build() {
	cmake -S "$_realname-$pkgver" -B build -GNinja -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr
	cmake --build build
}

package() {
	DESTDIR="$pkgdir" cmake --install build
}
