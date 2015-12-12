# Maintainer: Brian Bidulock <bidulock@openss7.org>
# Contributor: Robert Wiklund <robert@wikro.org>
# Contributor: carstene1ns <arch carsten-teibes de>

pkgname=libpthread-stubs
pkgver=0.3
pkgrel=6
pkgdesc="This library provides weak aliases for pthread functions not provided in libc or otherwise available by default."
arch=('i686' 'x86_64')
url="http://xcb.freedesktop.org/dist/"
license=('MIT')
source=("http://xcb.freedesktop.org/dist/${pkgname}-${pkgver}.tar.gz")
md5sums=('a09d928c4af54fe5436002345ef71138')
sha256sums=('3031f466cf0b06de6b3ccbf2019d15c4fcf75229b7d226a711bc1885b3a82cde')

build() {
  cd ${pkgname}-${pkgver}
  ./configure --prefix=/usr
  make
}

package() {
  cd ${pkgname}-${pkgver}
  make DESTDIR="${pkgdir}/" install
}

# vim:set ts=2 sw=2 et:
