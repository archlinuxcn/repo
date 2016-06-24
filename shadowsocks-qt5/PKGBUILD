# Maintainer: yk <yk at archlinuxcn dot org>

pkgname=shadowsocks-qt5
pkgver=2.7.0
pkgrel=2
pkgdesc="A fast, reliable and cross-platform GUI fronted for Shadowsocks."
arch=("i686" "x86_64")
url="http://github.com/librehat/$pkgname"
license=("GPL3")
depends=("qt5-base>=5.2" "botan-1.10>=1.10.12" "qrencode" "libqtshadowsocks>=1.8.4" "zbar" "libappindicator-activate-gtk2")
makedepends=("qtchooser" "git" "make")
provides=("$pkgname")
conflicts=("$pkgname")
source=("http://github.com/librehat/$pkgname/archive/v$pkgver.tar.gz")
sha256sums=('391107a084a232843718172c5a6a7eab2ef34b671aed90dd1187b2ab1a086941')

build() {
	cd "$srcdir/$pkgname-$pkgver"
	qmake INSTALL_PREFIX=/usr
	make
}

package() {
	cd "$srcdir/$pkgname-$pkgver"
	make INSTALL_ROOT="$pkgdir" install
}
