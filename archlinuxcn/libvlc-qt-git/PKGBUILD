# Maintainer: DDoSolitary <DDoSolitary@gmail.com>

pkgname=libvlc-qt-git
_pkgname=vlc-qt
pkgver=1.1.1.r7.g9b2f561
pkgrel=2
epoch=1
pkgdesc='A simple library to connect Qt application with libvlc'
arch=('i686' 'x86_64')
url='https://github.com/vlc-qt/vlc-qt'
license=('LGPL3')
depends=('vlc' 'qt5-declarative')
makedepends=('cmake' 'git')
provides=('libvlc-qt' 'libVLCQtCore.so' 'libVLCQtQml.so' 'libVLCQtWidgets.so')
conflicts=('libvlc-qt')
source=('git+https://github.com/vlc-qt/vlc-qt.git')
md5sums=('SKIP')

pkgver() {
	cd $_pkgname
	git describe --long | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

prepare() {
	mkdir -p build
}

build() {
	cd build
	cmake ../$_pkgname \
		-DCMAKE_INSTALL_PREFIX=/usr \
		-DSYSTEM_QML=ON
	make
}

package() {
	cd build
	make DESTDIR="$pkgdir/" install
}
