# Maintainer: Maxime Gauduin <alucryd@archlinux.org>
# Contributor: Jakub Schmidtke <sjakub-at-gmail-dot-com>
# Contributor: Kyle Keen <keenerd@gmail.com>
# Contributor: Dave Reisner <d@falconindy.com>

pkgname=lib32-jansson
pkgver=2.7
pkgrel=1
pkgdesc='C library for encoding, decoding and manipulating JSON data'
arch=('x86_64')
url='http://www.digip.org/jansson/'
depends=('jansson' 'lib32-glibc')
license=('MIT')
source=("http://www.digip.org/jansson/releases/jansson-${pkgver}.tar.bz2")
sha256sums=('459f2b7cf22fb676286723f26169a17cf111fbfb6f54e3dc2ec6b6f9f4a97bdc')

build() {
  cd jansson-${pkgver}

  export CC='gcc -m32'
  export CXX='g++ -m32'
  export PKG_CONFIG_PATH='/usr/lib32/pkgconfig'

  ./configure \
    --prefix='/usr' \
    --libdir='/usr/lib32'
  make
}

package() {
  cd jansson-${pkgver}

  make DESTDIR="${pkgdir}" install
  rm -rf "${pkgdir}"/usr/{share,include}

  install -dm 755 "${pkgdir}"/usr/share/licenses
  ln -s jansson "${pkgdir}"/usr/share/licenses/lib32-jansson
}

# vim:set ts=2 sw=2 et:
