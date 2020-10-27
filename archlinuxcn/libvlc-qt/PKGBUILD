# Maintainer: DDoSolitary <DDoSolitary@gmail.com>

pkgname=libvlc-qt
_pkgname=vlc-qt
pkgver=1.1.1
pkgrel=2
pkgdesc='A simple library to connect Qt application with libvlc'
arch=('i686' 'x86_64')
url='https://github.com/vlc-qt/vlc-qt'
license=('LGPL3')
depends=('vlc' 'qt5-declarative')
makedepends=('cmake')
provides=('libVLCQtCore.so' 'libVLCQtQml.so' 'libVLCQtWidgets.so')
source=("$_pkgname-$pkgver.tar.gz::https://github.com/vlc-qt/vlc-qt/archive/$pkgver.tar.gz")
sha256sums=('bdc8adb85d2c81e2b07630042e38b894b18882f74b3dbb97b33f357b50135bce')

prepare() {
	mkdir -p build
}

build() {
	cd build
	cmake ../$_pkgname-$pkgver \
		-DCMAKE_INSTALL_PREFIX=/usr \
		-DSYSTEM_QML=ON
	make
}

package() {
	cd build
	make DESTDIR="$pkgdir/" install
}
