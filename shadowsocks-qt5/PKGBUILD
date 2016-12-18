# Maintainer: yk <yk at archlinuxcn dot org>

pkgname=shadowsocks-qt5
pkgver=2.8.0
pkgrel=1
pkgdesc="A fast, reliable and cross-platform GUI fronted for Shadowsocks."
arch=("i686" "x86_64")
url="http://github.com/librehat/$pkgname"
license=("GPL3")
depends=("qt5-base>=5.2" "botan-1.10>=1.10.12" "qrencode" "libqtshadowsocks>=1.10" "zbar" "libappindicator-gtk2")
makedepends=("git" "make")
provides=("$pkgname")
conflicts=("$pkgname")
source=("http://github.com/librehat/$pkgname/archive/v$pkgver.tar.gz")
sha256sums=('dd983eb7de8a79346bd30a2b043baeaf24b1c54501ed6c7d4608dd54d2abb910')

build() {
	cd "$srcdir/$pkgname-$pkgver"
	qmake INSTALL_PREFIX=/usr
	make
}

package() {
	cd "$srcdir/$pkgname-$pkgver"
	make INSTALL_ROOT="$pkgdir" install
}
