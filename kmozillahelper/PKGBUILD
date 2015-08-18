# Contributor: Weng Xuetian <wengxt@gmail.com>
# Maintainer: Yegorius <yegorius@domic.us>

pkgname=kmozillahelper
pkgver=0.6.4
pkgrel=2
pkgdesc="Mozilla KDE Integration"
url="https://build.opensuse.org/package/show/openSUSE:Factory/mozilla-kde4-integration"
arch=("i686" "x86_64")
license=('MIT')
depends=("kdelibs")
makedepends=("cmake" "automoc4")
source=("${pkgname}-${pkgver}.tar.bz2::https://build.opensuse.org/source/openSUSE:Factory/mozilla-kde4-integration/${pkgname}-${pkgver}.tar.bz2")


build() {
	mkdir "$srcdir/$pkgname-build"
	cd "$srcdir/$pkgname-build"

	cmake -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Release "$srcdir/$pkgname"
	make || return 1
}

package() {
	cd "$srcdir/$pkgname-build"
	make DESTDIR="$pkgdir" install
}

md5sums=('7db8c8904371204fb4c13e9cd306deb0')
