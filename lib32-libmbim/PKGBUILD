# Maintainer: Maxime Gauduin <alucryd@archlinux.org>
# Contributor: Jan Alexander Steffens (heftig) <jan.steffens@gmail.com>

pkgname=lib32-libmbim
pkgver=1.12.0
pkgrel=1
pkgdesc='MBIM modem protocol helper library'
arch=('x86_64')
url='http://www.freedesktop.org/wiki/Software/libmbim/'
license=('GPL2')
depends=('lib32-systemd' 'libmbim')
makedepends=('gcc-multilib' 'python')
source=("http://www.freedesktop.org/software/libmbim/libmbim-${pkgver}.tar.xz")
sha256sums=('b5b9e72d6b0a4d9e5a92b913c16426946f8f6cf60e648635306ebade44ace553')

build() {
  cd libmbim-${pkgver}

  export CC='gcc -m32'
  export CXX='g++ -m32'
  export PKG_CONFIG_PATH='/usr/lib32/pkgconfig'

  ./configure \
    --prefix='/usr' \
    --libdir='/usr/lib32' \
    --libexecdir='/usr/lib32/libmbim' \
    --localstatedir='/var' \
    --sysconfdir='/etc' \
    --disable-gtk-doc-html \
    --disable-static \
    --without-python
  make
}

package() {
  cd libmbim-${pkgver}

  make DESTDIR="${pkgdir}" install
  rm -rf "${pkgdir}"/usr/{bin,include,share}
}

# vim: ts=2 sw=2 et:
