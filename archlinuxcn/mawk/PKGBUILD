# Maintainer: zoorat <zoorat [at] protonmail [dot] com>
# Contributor: judd <jvinet@zeroflux.org>
# Contributor: Judd Vinet <jvinet@zeroflux.org>
# Contributor: Stefan Husmann <stefan-husmann@t-online.de>

pkgname=mawk
pkgver=1.3.4_20240123
pkgrel=1

pkgdesc="An interpreter for the AWK Programming Language"
arch=('i686' 'x86_64')
url="http://invisible-island.net/mawk/"
license=('GPL')

depends=('glibc')
changelog="changelog.txt"

source=("https://invisible-island.net/archives/$pkgname/$pkgname-${pkgver//_/-}.tgz")
b2sums=('29a9c89995e969a62bd0b30e494c67e53aea0466c9286e2005422a54a44bef661ef6223522c4b51bc49b83c56512ae47e784c237dd39dfef77b7aa13ec33973a')

build() {
	cd $pkgname-${pkgver/_/-}
	sed -ie 's|log()|log(1.0)|g' configure
	sed -ie "s|trap  *0|trap 'exit 0' 0|g" test/*
	./configure
	make
}

package() {
	cd $pkgname-${pkgver/_/-}
	install -d "$pkgdir"/usr/bin
	install -d "$pkgdir"/usr/share/man/
	make BINDIR="$pkgdir"/usr/bin MANDIR="$pkgdir"/usr/share/man/ install
}
