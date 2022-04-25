# Maintainer: HurricanePootis <hurricanepootis@protonmail.com>
# Contributor: Spike29 <leguen.yannick@gmail.com>
# Contributor: Samir Faci <csgeek@archlinux.us>
# Contributor: TimothÃ©e Ravier <tim@siosm.fr>

pkgbase=qxmpp
pkgname=('qxmpp' 'qxmpp-doc')
pkgver=1.4.0
pkgrel=2
pkgdesc='Cross-platform C++ XMPP client and server library'
arch=('i686' 'x86_64')
url='https://github.com/qxmpp-project/qxmpp'
license=('LGPL2.1')
depends=('qt5-base' 'gstreamer')
makedepends=('cmake' 'doxygen')
source=("${url}/archive/v${pkgver}.tar.gz")
sha256sums=('2148162138eaf4b431a6ee94104f87877b85a589da803dff9433c698b4cf4f19')

prepare() {
	cd "$srcdir/$pkgname-$pkgver"
	[ -d build ] || mkdir build
	sed -i "s|^.*find_package(QT NAMES Qt6 Qt5 REQUIRED COMPONENTS Core Network Xml).*$|set(QT_VERSION_MAJOR 5)|" CMakeLists.txt
}

build() {
	cd "$srcdir/$pkgname-$pkgver/build"
	
	cmake -DCMAKE_INSTALL_PREFIX=/usr \
	-DBUILD_DOCUMENTATION=1 \
	-DCMAKE_INSTALL_LIBDIR=lib \
	-DBUILD_EXAMPLES=0 \
	-DBUILD_TESTS=0 \
	-DWITH_GSTREAMER=1 \
	..
	make
}

package_qxmpp() {
	cd "$srcdir/$pkgname-$pkgver/build"
	make DESTDIR="$pkgdir" install
	rm -rf "$pkgdir/usr/share/doc"
}

package_qxmpp-doc(){
	pkgdesc='Cross-platform C++ XMPP client and server library (documentation)'
	arch=('any')
	cd "$srcdir/$pkgbase-$pkgver/build"
	make DESTDIR="$pkgdir" install
	rm -rf "$pkgdir/usr/include"
	rm -rf "$pkgdir/usr/lib"
}
