# Maintainer: HurricanePootis <hurricanepootis@protonmail.com>
# Contributor: Spike29 <leguen.yannick@gmail.com>
# Contributor: Samir Faci <csgeek@archlinux.us>
# Contributor: TimothÃ©e Ravier <tim@siosm.fr>

pkgbase=qxmpp
pkgname=('qxmpp' 'qxmpp-doc')
pkgver=1.5.2
pkgrel=1
pkgdesc='Cross-platform C++ XMPP client and server library'
arch=('i686' 'x86_64')
url='https://github.com/qxmpp-project/qxmpp'
license=('LGPL2.1')
depends=('qt5-base' 'gstreamer')
makedepends=('cmake' 'doxygen')
source=("${url}/archive/v${pkgver}.tar.gz")
sha256sums=('cc26345428d816bb33e63f92290c52b9a417d9a836bf9fabf295e3477f71e66c')

prepare() {
	cd "$srcdir/$pkgname-$pkgver"
	sed -i "s|^.*find_package(QT NAMES Qt6 Qt5 REQUIRED COMPONENTS Core Network Xml).*$|set(QT_VERSION_MAJOR 5)|" CMakeLists.txt
}

build() {
	cd "$srcdir"
	
	cmake -S $pkgname-$pkgver -B build \
	-DCMAKE_INSTALL_PREFIX=/usr \
	-DBUILD_DOCUMENTATION=1 \
	-DCMAKE_INSTALL_LIBDIR=lib \
	-DBUILD_EXAMPLES=0 \
	-DBUILD_TESTS=0 \
	-DWITH_GSTREAMER=1

	cmake --build build
}

package_qxmpp() {
	cd "$srcdir"
	DESTDIR="$pkgdir" cmake --install build
	rm -rf "$pkgdir/usr/share"
}

package_qxmpp-doc(){
	pkgdesc='Cross-platform C++ XMPP client and server library (documentation)'
	arch=('any')
	cd "$srcdir"
	DESTDIR="$pkgdir" cmake --install build
	rm -rf "$pkgdir/usr/include"
	rm -rf "$pkgdir/usr/lib"
}
