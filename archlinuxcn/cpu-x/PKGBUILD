# Maintainer: X0rg

_realname=CPU-X
pkgname=cpu-x
pkgver=4.4.0
pkgrel=2
pkgdesc="A Free software that gathers information on CPU, motherboard and more"
arch=('i686' 'x86_64')
url="http://X0rg.github.io/CPU-X/"
license=('GPL3')
depends=('gtk3' 'ncurses' 'libcpuid' 'pciutils' 'glfw' 'opencl-icd-loader' 'vulkan-icd-loader' 'procps-ng')
makedepends=('cmake' 'ninja' 'nasm' 'opencl-headers' 'vulkan-headers')
optdepends=('opencl-driver: packaged openCL driver'
            'opengl-driver: packaged openGL driver'
            'vulkan-driver: packaged Vulkan driver')
source=("$pkgname-$pkgver.tar.gz::https://github.com/X0rg/CPU-X/archive/v$pkgver.tar.gz")
sha512sums=('57c960f6c3007455f4d36ccc6d500b18195b305b3d3bdbbdc4b6804f9c1219460c31f854f38d18a49b1c4c0b870970cfcfe6abae4e5c0cdc83e452c5614c13fb')

build() {
	cmake -S "$_realname-$pkgver" -B build -GNinja -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_INSTALL_LIBEXECDIR="lib/cpu-x"
	cmake --build build
}

package() {
	DESTDIR="$pkgdir" cmake --install build
}
