# Maintainer: zoorat <zoorat [at] protonmail [dot] com>
# Contributor: judd <jvinet@zeroflux.org>
# Contributor: Judd Vinet <jvinet@zeroflux.org>
# Contributor: Stefan Husmann <stefan-husmann@t-online.de>

pkgname=mawk
pkgver=1.3.4_20231102
pkgrel=3

pkgdesc="An interpreter for the AWK Programming Language"
arch=('i686' 'x86_64')
url="http://invisible-island.net/mawk/"
license=('GPL')

depends=('glibc')
changelog="changelog.txt"

source=("https://invisible-island.net/archives/$pkgname/$pkgname-${pkgver//_/-}.tgz")
b2sums=('c423381900be429dcfb117df3ceb72dc942aec6e85ea94e59b2fef1b92445620cff3205fb55be1ddee2bfba9597a1c68ed2f41bb155a1cc6791df0f6de75b44b')

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
