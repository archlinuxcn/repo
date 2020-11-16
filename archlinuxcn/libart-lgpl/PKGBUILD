#!/hint/bash
# Maintainer : bartus <arch-user-repo[at]bartus.33mail.com>
# Contributor : Jan de Groot <jgc@archlinux.org>
# shellcheck disable=SC2034,SC2154 #unused uninitialized variable
# shellcheck disable=SC2164 #cd safe

pkgname=libart-lgpl
pkgver=2.3.21
pkgrel=5
pkgdesc="A library for high-performance 2D graphics"
url="https://www.levien.com/libart/"
arch=('x86_64')
license=('LGPL')
source=("https://download.gnome.org/sources/libart_lgpl/2.3/libart_lgpl-${pkgver}.tar.bz2")
sha256sums=('fdc11e74c10fc9ffe4188537e2b370c0abacca7d89021d4d303afdf7fd7476fa')

build() {
  cd "${srcdir}/libart_lgpl-${pkgver}"
  ./configure --prefix=/usr --disable-static
  make
}

package() {
  cd "${srcdir}/libart_lgpl-${pkgver}"
  make DESTDIR="${pkgdir}" install
}
