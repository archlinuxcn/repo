#Maintainer: Andrew Bibb <ajbibb@myfairpoint.net>
pkgname=cmst
pkgver=2018.01.06
pkgrel=1
pkgdesc="A QT based GUI front end for the connman connection manager with systemtray icon"
arch=('i686' 'x86_64')
url="https://github.com/andrew-bibb/cmst"
license=('MIT (Expat)')
depends=('qt5-base' 'connman' 'libxkbcommon-x11' 'hicolor-icon-theme')
source=(https://github.com/andrew-bibb/cmst/releases/download/${pkgname}-${pkgver}/${pkgname}-${pkgver}.tar.xz)

md5sums=('f2f08754c1e189f6a1643786a4139de1')

build() {
	cd "$srcdir/$pkgname-$pkgver"
	qmake-qt5 DISTRO=arch
	make 
}


package() {
	cd "$srcdir/$pkgname-$pkgver"
	make INSTALL_ROOT="$pkgdir/" install
}
