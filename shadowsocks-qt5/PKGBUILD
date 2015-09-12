# Maintainer: yk <yk at archlinuxcn dot org>

pkgname=shadowsocks-qt5
pkgver=2.4.2
pkgrel=2
pkgdesc="A fast, reliable and cross-platform GUI fronted for Shadowsocks."
arch=("i686" "x86_64")
url="http://github.com/librehat/$pkgname"
license=("GPL3")
depends=("qt5-base>=5.2" "botan-1.10" "qrencode" "libqtshadowsocks>=1.4.2" "zbar" "libappindicator-gtk2")
makedepends=("qtchooser" "git" "make")
provides=("$pkgname")
conflicts=("$pkgname")
install=$pkgname.install

source=("http://github.com/librehat/$pkgname/archive/v$pkgver.tar.gz"
        "shadowsocks-qt5.install"
)
sha1sums=('e3d2fd414a4959fc60f7d8c3564d1c8f4d4146f5'
        'c54b62265d83554e71c98c69511937e1f01911c3'
)

build() {
	cd "$srcdir/$pkgname-$pkgver"
	qmake INSTALL_PREFIX=/usr
	make
}

package() {
	cd "$srcdir/$pkgname-$pkgver"
	make INSTALL_ROOT="$pkgdir" install
}
