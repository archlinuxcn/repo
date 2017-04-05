# Maintainer: Brian Bidulock <bidulock@openss7.org>
# Contributor: Robert Wiklund <robert@wikro.org>
# Contributor: carstene1ns <arch carsten-teibes de>

pkgname=libpthread-stubs
pkgver=0.4
pkgrel=1
pkgdesc="This library provides weak aliases for pthread functions not provided in libc or otherwise available by default."
arch=('i686' 'x86_64')
url="http://xcb.freedesktop.org/dist/"
license=('MIT')
source=("http://xcb.freedesktop.org/dist/${pkgname}-${pkgver}.tar.gz")
md5sums=('7d2734e604a3e2f6f665c420b835ab62')
sha256sums=('50d5686b79019ccea08bcbd7b02fe5a40634abcfd4146b6e75c6420cc170e9d9')

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
