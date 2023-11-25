# Maintainer: UnicornDarkness

_realname=CPU-X
pkgname=cpu-x
pkgver=5.0.2
pkgrel=1
pkgdesc="A Free software that gathers information on CPU, motherboard and more"
arch=('i686' 'x86_64')
url="https://thetumultuousunicornofdarkness.github.io/CPU-X"
license=('GPL3')
depends=('gtkmm3' 'ncurses' 'libcpuid>=0.6.0' 'pciutils' 'glfw' 'vulkan-icd-loader' 'procps-ng>=4.0.0')
makedepends=('cmake' 'ninja' 'nasm' 'vulkan-headers')
optdepends=('opengl-driver: packaged openGL driver'
            'vulkan-driver: packaged Vulkan driver')
source=("$pkgname-$pkgver.tar.gz::https://github.com/TheTumultuousUnicornOfDarkness/CPU-X/archive/v$pkgver.tar.gz")
sha512sums=('3677207af8ea233a5bc1e435f501f4dffbe555486b048f5b51ac818cb458d52ab7ac94830ab83e992772e339de93464b3d4cd92798b8f49a272fd5292484de7e')

build() {
	cmake -S "$_realname-$pkgver" -B build -GNinja -DCMAKE_BUILD_TYPE=Release -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_INSTALL_LIBEXECDIR="lib/cpu-x"
	cmake --build build
}

check() {
	ninja -C build test
}

package() {
	DESTDIR="$pkgdir" cmake --install build
}
