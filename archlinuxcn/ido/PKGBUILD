# Maintainer: Maxime Gauduin <alucryd@archlinux.org>
# Contributor: Balló György <ballogyor+arch@gmail.com>

pkgname=ido
pkgver=12.10.2
pkgrel=4
pkgdesc='Widgets and other objects used for indicators'
arch=('i686' 'x86_64')
url='https://launchpad.net/ido'
license=('LGPL')
depends=('gtk3')
source=("https://launchpad.net/ido/${pkgver%.*}/${pkgver}/+download/ido-${pkgver}.tar.gz")
sha256sums=('e2279c7c0eeeb2e038eaf87418df109327de28c758f45e72e19c7154a1f71f00')

build() {
  cd ido-${pkgver}

  export CFLAGS="$CFLAGS -Wno-deprecated-declarations"

  ./configure \
    --prefix='/usr' \
    --localstatedir='/var' \
    --sysconfdir='/etc'
  make
}

package(){
  cd ido-${pkgver}

  make DESTDIR="${pkgdir}" install
}

# vim: ts=2 sw=2 et:
