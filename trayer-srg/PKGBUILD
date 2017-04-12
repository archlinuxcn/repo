# Maintainer: Shengyu Zhang <lastavengers at archlinuxcn dot org>
# Contributor: wallnuss <v dot churavy at gmail dot com>

pkgname=trayer-srg
pkgver=1.1.7
pkgrel=1
pkgdesc="trayer fork with multi monitor support, cleaned up codebase and other fancy stuff"
arch=('i686' 'x86_64')
url="https://github.com/sargon/trayer-srg"
license=('MIT')
depends=('gtk2')
conflicts=('trayer' 'trayer-srg-git')
replaces=('trayer' 'trayer-srg-git')
provides=('trayer-srg')
source=("https://github.com/sargon/${pkgname}/archive/trayer-${pkgver}.tar.gz")
sha256sums=('145de7081a338d0334f4d0fad73f1fcd08d3b32ebbf865eb99cf6f18bf02eb49')

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
