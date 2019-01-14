# Maintainer: aksr <aksr at t-com dot me>
pkgname=libeb
_pkgname=eb
pkgver=4.4.3
pkgrel=1
epoch=
pkgdesc="A C library for accessing CD-ROM books, supports EB, EBG, EBXA, EBXA-C, S-EBXA and EPWING formats."
arch=('i686' 'x86_64')
url="ftp://ftp.sra.co.jp/pub/misc/eb/"
url="http://www.sra.co.jp/people/m-kasahr/eb/"
license=('GPLv2')
groups=()
depends=()
makedepends=()
checkdepends=()
optdepends=()
provides=()
conflicts=()
replaces=()
backup=()
options=()
install=
changelog=
source=("ftp://ftp.sra.co.jp/pub/misc/eb/${_pkgname}-${pkgver}.tar.bz2")
noextract=()
md5sums=('17dd1fade7ba0b82ce6e60f19fcbc823')
sha1sums=('1cc55c90fcac224bf299289e7a0fe1559f0761ab')
sha256sums=('abe710a77c6fc3588232977bb2f30a2e69ddfbe9fa8d0b05b0d67d95e36f4b5f')

build() {
  cd "$srcdir/${_pkgname}-${pkgver}"
  ./configure --prefix=/usr
  make
}

check() {
  cd "$srcdir/${_pkgname}-${pkgver}"
  make -k check
}

package() {
  cd "$srcdir/${_pkgname}-${pkgver}"
  make DESTDIR="$pkgdir/" install
}

