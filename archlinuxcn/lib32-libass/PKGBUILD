# Contributor: GordonGR <ntheo1979@gmail.com>
# Contributor: Johannes Dewender  arch at JonnyJD dot net
# Contributor: jospehgbr <rafael.f.f1@gmail.com>
# Maintainer: Adam <adam900710@gmail.com>

_pkgname=libass
pkgname=lib32-${_pkgname}
pkgver=0.14.0
pkgrel=3
pkgdesc='A portable library for SSA/ASS subtitles rendering (32 bit)'
arch=('x86_64')
url='https://github.com/libass/libass/'
license=('BSD')
depends=("${_pkgname}" 'lib32-fontconfig' 'lib32-fribidi' 'lib32-glib2' 'lib32-glibc'
         'libfreetype.so')
makedepends=('gcc-multilib' 'nasm')
provides=('libass.so')
source=("https://github.com/libass/libass/releases/download/${pkgver}/libass-${pkgver}.tar.xz")
sha256sums=('881f2382af48aead75b7a0e02e65d88c5ebd369fe46bc77d9270a94aa8fd38a2')

build() {
  cd "${_pkgname}-${pkgver}"
  export PKG_CONFIG_PATH='/usr/lib32/pkgconfig'
  export CC='gcc -m32'

  ./configure \
    --prefix='/usr' \
    --libdir='/usr/lib32' \
    --host=i686-linux-gnu \
    --enable-harfbuzz \
    --enable-fontconfig
  make
}

package() {
  cd "${_pkgname}-${pkgver}"

  make DESTDIR="${pkgdir}" install
  install -Dm 644 COPYING -t "${pkgdir}"/usr/share/licenses/${pkgname}/
  rm -rf "${pkgdir}"/usr/include
}

# vim: ts=2 sw=2 et:
