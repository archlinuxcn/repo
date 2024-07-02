# Maintainer: zoorat <zoorat [at] protonmail [dot] com>
# Contributor: judd <jvinet@zeroflux.org>
# Contributor: Judd Vinet <jvinet@zeroflux.org>
# Contributor: Stefan Husmann <stefan-husmann@t-online.de>

pkgname=mawk
pkgver=1.3.4_20240622
pkgrel=1

pkgdesc="An interpreter for the AWK Programming Language"
arch=('i686' 'x86_64')
url="http://invisible-island.net/mawk/"
license=('GPL')

depends=('glibc')
changelog="changelog.txt"

source=("https://invisible-island.net/archives/$pkgname/$pkgname-${pkgver//_/-}.tgz")
b2sums=('3238e633546ea04b0e3822271fcd37d1ac6ae3924c9e7655ff14c9fa35d691ba27bb779e7c1b7f95a46c0aa90b75a71ab2681763c89812f55773e97489e03ff8')

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
