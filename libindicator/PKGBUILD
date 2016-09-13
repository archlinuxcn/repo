# Maintainer: Llewelyn Trahaearn <WoefulDerelict at GMail dot com>
# Contributor: Yurii Kolesnykov <yurikoles at gmail dot com>
# Contributor: Gustavo <sl1pkn07 at gmail dot com>
# Contributor: Maxime Gauduin <alucryd at archlinux dot org>
# Contributor: Balló György <ballogyor+arch at gmail dot com>

pkgbase=libindicator
pkgname=("${pkgbase}-gtk"{2,3})
pkgver=12.10.1
pkgrel=6
pkgdesc='A set of symbols and convenience functions for Ayatana indicators.'
arch=('i686' 'x86_64')
url='https://launchpad.net/libindicator'
license=('GPL3')
makedepends=('gtk2' 'gtk3')
source=("https://launchpad.net/${pkgbase}/${pkgver%.*}/${pkgver}/+download/${pkgbase}-${pkgver}.tar.gz")
sha512sums=('d6d77d0309b15cf6b52539323920ab0c1594cb1c1cef8a8d67cd0f76f8ceeeac28eb6db6227563df1932e6f1fadcffac68d82982182b745257dfaf91f1c945af')

prepare() {
  # Check for debris from previous builds and sweep it up if found.
  [[ -d ${pkgbase}-gtk2 ]] && rm -rf ${pkgbase}-gtk2
  [[ -d ${pkgbase}-gtk3 ]] && rm -rf ${pkgbase}-gtk3

  sed '/-Werror/s/$/ -Wno-deprecated-declarations/' -i ${pkgbase}-${pkgver}/${pkgbase}/Makefile.{am,in}
  sed 's/LIBINDICATOR_LIBS+="$LIBM"/LIBINDICATOR_LIBS+=" $LIBM"/g' -i ${pkgbase}-${pkgver}/configure
  sed 's/LIBM="-lmw"/LIBM=" -lmw"/g' -i ${pkgbase}-${pkgver}/configure
  sed 's/LIBM="-lm"/LIBM=" -lm"/g' -i ${pkgbase}-${pkgver}/configure
  sed 's/LIBS="-lm  $LIBS"/LIBS=" -lm  $LIBS"/g' -i ${pkgbase}-${pkgver}/configure
  sed 's/LIBS="-lmw  $LIBS"/LIBS=" -lmw  $LIBS"/g' -i ${pkgbase}-${pkgver}/configure

  mkdir -p ${pkgbase}-gtk{2,3}
}

build() {
  cd ${pkgbase}-gtk3
  ../libindicator-${pkgver}/configure \
    --prefix='/usr' \
    --localstatedir='/var' \
    --libexecdir='/usr/lib/libindicator' \
    --sysconfdir='/etc' \
    --disable-static \
    --disable-tests
  make

  cd ${srcdir}/${pkgbase}-gtk2
  ../libindicator-${pkgver}/configure \
    --prefix='/usr' \
    --localstatedir='/var' \
    --libexecdir='/usr/lib/libindicator' \
    --sysconfdir='/etc' \
    --with-gtk='2' \
    --disable-static \
    --disable-tests
  make
}

package_libindicator-gtk2() {
  depends=('gtk2')
  provides=("${pkgbase}")
  conflicts=("${pkgbase}")

  cd ${pkgbase}-gtk2
  make -j1 DESTDIR="${pkgdir}" install
  rm -rf "${pkgdir}"/usr/share
}

package_libindicator-gtk3() {
  depends=('gtk3')
  provides=("${pkgbase}3")
  conflicts=("${pkgbase}3")

  cd ${pkgbase}-gtk3
  make -j1 DESTDIR="${pkgdir}" install
  rm -rf "${pkgdir}"/usr/share
}
