# Maintainer: Shengyu Zhang <la@archlinuxcn.org>
# Contributor: wallnuss <v dot churavy at gmail dot com>

pkgname=trayer-srg
pkgver=1.1.8
pkgrel=2
pkgdesc="trayer fork with multi monitor support, cleaned up codebase and other fancy stuff"
arch=('i686' 'x86_64')
url="https://github.com/sargon/trayer-srg"
license=('MIT')
depends=('gtk2')
conflicts=('trayer' 'trayer-srg-git')
provides=('trayer-srg')
source=("https://github.com/sargon/${pkgname}/archive/trayer-${pkgver}.tar.gz")
sha256sums=('c62e5a700618511f2e51c225d3536945eeb60d4680f2b66fde30e64788dcefaa')

_srcdir=${pkgname}-trayer-${pkgver}

build() {
  cd ${_srcdir}
  ./configure --prefix="${pkgdir}/usr"
  make
}

package() {
  cd ${_srcdir}
  make install

  install -D -m644 man/trayer.1 "${pkgdir}/usr/share/man/man1/trayer.1"
  install -D -m644 COPYING "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
