# Maintainer: Manuel Coenen <manuel.coenen@gmail.com>
pkgname=timg
pkgver=1.6.3
pkgrel=2
pkgdesc="Terminal Image and Video Viewer"
arch=('any')
url="https://github.com/hzeller/timg"
license=('GPL2')
depends=('libwebp' 'libjpeg-turbo' 'libexif' 'graphicsmagick' 'ffmpeg' 'openslide' 'libsixel' 'libdeflate' 'librsvg' 'poppler-glib')
makedepends=('cmake' 'pkgconf' 'git' 'gcc')
source=("timg-$pkgver.tar.gz::https://github.com/hzeller/timg/archive/v$pkgver.tar.gz")
sha256sums=('59c908867f18c81106385a43065c232e63236e120d5b2596b179ce56340d7b01')

build() {
	cd "$pkgname-$pkgver"
	rm -rf build
	mkdir build
	cd build
	cmake ../ \
		-DCMAKE_GENERATOR="Unix Makefiles" \
		-DCMAKE_INSTALL_PREFIX="${pkgdir}/usr" \
		-DWITH_VIDEO_DEVICE=On \
		-DWITH_OPENSLIDE_SUPPORT=On \
		-DWITH_STB_IMAGE=Off
	make
}

package() {
	cd "$pkgname-$pkgver"/build
	install -d "${pkgdir}/usr/"{bin,share/man/man1}
	make install
}
