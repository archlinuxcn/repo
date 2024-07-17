# Maintainer: kleintux <reg-archlinux AT klein DOT tuxli DOT ch> 

pkgname=principia
pkgver=2024.07.12
pkgrel=1
pkgdesc="Physics-based sandbox building game."
url='https://github.com/Bithack/principia/'
arch=('x86_64' 'i686')
license=('bsd-3')
depends=('gtk3' 'glew' 'curl' 'libpng' 'libjpeg' 'freetype2' 'sdl2' 'sdl2_image' 'sdl2_mixer' 'sdl2_ttf')
makedepends=('cmake' 'ninja')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/Bithack/principia/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('6cb1be280f6e79fe7782f3a43966d2ae34d2470bf14c5085d1cc761c29547f12')

build() {
	cd "${pkgname}-${pkgver}"
	mkdir -p build
	cd build
	cmake .. -G Ninja -DCMAKE_INSTALL_PREFIX=/usr
	ninja
}

package() {
	cd "${pkgname}-${pkgver}/build"
	DESTDIR="${pkgdir}" ninja install
}
