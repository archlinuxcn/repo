# Maintainer: Adrian Perez de Castro <aperez@igalia.com>
# Contributor: Tom < reztho at archlinux dot org >
# Based on the munt-git package from Franco Tortoriello
pkgname=munt
pkgdesc='Software synthesizer emulating pre-GM MIDI devices such as the Roland MT-32, CM-32L, CM-64 and LAPC-I'
pkgver=2.7.0
pkgrel=1
arch=('i686' 'x86_64')
url=http://munt.sourceforge.net
license=('GPL2')
depends=('qt5-multimedia' 'portaudio' 'hicolor-icon-theme')
makedepends=('cmake')
install=${pkgname}.install
source=("$pkgname-$pkgver.tar.gz::https://sourceforge.net/projects/$pkgname/files/$pkgname/$pkgver/$pkgname-$pkgver.tar.gz/download")
b2sums=('099beab9a568bbe9775730a8bf4d541ea367a78e12d726f3b1cd418d7b6d802f2d8680fa29a005f43b5b8c5f0a942f3ad95f120d295be71b77c379c5adb3f2c7')

build() {
	rm -rf _build
	cmake -S"$startdir/src/$pkgname-$pkgver" -B_build \
		-DBUILD_SHARED_LIBS=ON \
		-DCMAKE_INSTALL_PREFIX=/usr \
		-Dmunt_WITH_MT32EMU_QT=ON \
		-Dmunt_WITH_MT32EMU_SMF2WAV=OFF
	make -C_build
}

package() {
	make -C_build DESTDIR="${pkgdir}" install
}
