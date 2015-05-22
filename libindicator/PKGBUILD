# Maintainer: Maxime Gauduin <alucryd@archlinux.org>
# Contributor: Balló György <ballogyor+arch@gmail.com>

pkgbase=libindicator
pkgname=('libindicator-gtk2' 'libindicator-gtk3')
pkgver=12.10.1
pkgrel=4
pkgdesc='A set of symbols and convenience functions for Ayatana indicators'
arch=('i686' 'x86_64')
url="https://launchpad.net/${pkgbase}"
license=('GPL')
makedepends=('gtk2' 'gtk3')
source=("https://launchpad.net/${pkgbase}/${pkgver%.*}/${pkgver}/+download/${pkgname%-*}-${pkgver}.tar.gz")
sha256sums=('b2d2e44c10313d5c9cd60db455d520f80b36dc39562df079a3f29495e8f9447f')

prepare() {
  sed '/-Werror/s/$/ -Wno-deprecated-declarations/' -i ${pkgbase}-${pkgver}/libindicator/Makefile.{am,in}
  cp -r ${pkgbase}-${pkgver} ${pkgbase}-gtk2-${pkgver}
}

build() {
  cd ${pkgbase}-${pkgver}

  ./configure --prefix='/usr' --sysconfdir='/etc' --localstatedir='/var' \
              --libexecdir="/usr/lib/${pkgbase}" --disable-{static,tests}
  make -j1

  cd ../${pkgbase}-gtk2-${pkgver}

  ./configure --prefix='/usr' --sysconfdir='/etc' --localstatedir='/var' \
              --libexecdir="/usr/lib/${pkgbase}" --disable-{static,tests} \
              --with-gtk='2'
  make -j1
}

package_libindicator-gtk2() {
  depends=('gtk2')
  provides=('libindicator')
  conflicts=('libindicator')

  cd ${pkgbase}-gtk2-${pkgver}

  make -j1 DESTDIR="${pkgdir}" install
  rm -rf "${pkgdir}"/usr/share
}

package_libindicator-gtk3() {
  depends=('gtk3')
  provides=('libindicator3')
  conflicts=('libindicator3')

  cd ${pkgbase}-${pkgver}

  make -j1 DESTDIR="${pkgdir}" install
  rm -rf "${pkgdir}"/usr/share
}

# vim: ts=2 sw=2 et:
