# Contributor: judd <jvinet@zeroflux.org>
# Committer: Judd Vinet <jvinet@zeroflux.org>
# Maintainer: Stefan Husmann <stefan-husmann@t-online.de>

pkgname=mawk
pkgver=1.3.4_20230808
pkgrel=1
pkgdesc="An interpreter for the AWK Programming Language"
arch=('i686' 'x86_64')
license=('GPL')
depends=('glibc')
url="http://invisible-island.net/mawk/"
source=("https://invisible-island.net/archives/$pkgname/$pkgname-${pkgver//_/-}.tgz")
sha256sums=('88f55a632e2736ff5c5f69944abc151734d89d8298d5005921180f39ab7ba6d0')

build() {
  cd $pkgname-${pkgver/_/-}
  sed -ie 's|log()|log(1.0)|g' configure
  sed -ie "s|trap  *0|trap 'exit 0' 0|g" test/*
  ./configure 
  make -j1 
}

package () {
  cd $pkgname-${pkgver/_/-}
  install -d "$pkgdir"/usr/bin
  install -d "$pkgdir"/usr/share/man/man1
  make BINDIR="$pkgdir"/usr/bin \
    MANDIR="$pkgdir"/usr/share/man/man1 install 
}
