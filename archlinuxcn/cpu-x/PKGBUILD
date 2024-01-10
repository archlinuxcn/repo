# Maintainer: UnicornDarkness

_realname=CPU-X
pkgname=cpu-x
pkgver=5.0.3
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
sha512sums=('d9a29a5303101a6c00d9145265d85acec865833f175246bde550ba2dff24a924c1b2de7579b3d8e20aa163092d269af9bbb24e073585d3e18a2c726e48d9be41')

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
