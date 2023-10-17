# Maintainer: UnicornDarkness

_realname=CPU-X
pkgname=cpu-x
pkgver=5.0.0
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
sha512sums=('c4fd7247c83987ab1c84586317a95327809510ed1289cd32cc16cd4d46c8d6af58f8496342e9172ad06cb8189d3e4c82a4826e9c8054fa2dc8cdd166ac29436d')

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
