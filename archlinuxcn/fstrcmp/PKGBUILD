# Contributor: Sergio Tridente <tioduke at gmail dot com>

pkgname=fstrcmp
pkgver=0.7.D001
pkgrel=3
pkgdesc="A library that is used to make fuzzy comparisons of strings and byte arrays, including multi-byte character strings"
arch=('i686' 'x86_64')
url="http://fstrcmp.sourceforge.net/"
license=('GPL')
depends=('glibc')
makedepends=('make' 'gcc' 'ghostscript' 'groff' 'libtool')
options=(!libtool !staticlibs)
source=(http://fstrcmp.sourceforge.net/$pkgname-$pkgver.tar.gz)
md5sums=('9c440bbdfcad9fd22e38f2388715b0cc')
noextract=("$pkgname-$pkgver.tar.gz")


prepare() {
  cd "$srcdir"
  tar -zxvf $pkgname-$pkgver.tar.gz
}

build() {
  cd "$srcdir/$pkgname-$pkgver"
  ./configure --prefix=/usr
  make
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  mkdir -p "${pkgdir}"/usr/bin
  make DESTDIR="${pkgdir}" install
}
