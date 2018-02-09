pkgname=gammaray
pkgver=2.9.0
pkgrel=1
epoch=
pkgdesc="A tool for examining the internals of a Qt application and to some extent also manipulate it"
arch=('i686' 'x86_64')
url="http://www.kdab.com/gammaray/"
license=('GPL')
makedepends=(cmake perl)
depends=(graphviz
	#qt5-3d			# 3D-Render
	#qt5-connectivity	# Bluetooth
	qt5-declarative		# QML
	qt5-location		# Positioning plugin
	qt5-script		# QtScript debugging
	qt5-svg 		# SVG export
	qt5-tools		# Widget .ui file export
	qt5-webkit		# Web inspector
)
source=(https://github.com/KDAB/GammaRay/archive/v$pkgver.tar.gz)
sha256sums=('f86159c77cff4aaf22feed6fb2ee012028df179f54e0e441642115f93ffc41b5')
build() {
	cd "$srcdir/GammaRay-$pkgver"
	mkdir -p build
	cd build
	cmake .. \
		-DCMAKE_BUILD_TYPE=Release \
		-DCMAKE_INSTALL_PREFIX=/usr \
		-DECM_MKSPECS_INSTALL_DIR=/usr/lib/qt/mkspecs/modules
	make
}

package() {
	cd "$srcdir/GammaRay-$pkgver/build"
	make DESTDIR="$pkgdir/" install
}
