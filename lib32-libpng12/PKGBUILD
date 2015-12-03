# Maintainer: Arthur Zamarin <arthurzam@gmail.com>
# Contributor: trya <tryagainprod@gmail.com>
# Contributor: Jan de Groot <jgc@archlinux.org>
# Contributor: dorphell <dorphell@archlinux.org>
# Contributor: Travis Willard <travis@archlinux.org>
# Contributor: Douglas Soares de Andrade <douglas@archlinux.org>

_pkgbasename=libpng
pkgname=lib32-libpng12
pkgver=1.2.54
pkgrel=2
pkgdesc="A collection of routines used to create PNG format graphics files (32-bit, 1.2 branch)"
arch=('x86_64')
url="http://www.libpng.org/pub/png/libpng.html"
license=('custom')
depends=('lib32-zlib' 'libpng12')
makedepends=('gcc-multilib') 
options=('!libtool')
source=("http://sourceforge.net/projects/libpng/files/libpng12/${pkgver}/libpng-${pkgver}.tar.xz"
        "http://sourceforge.net/projects/apng/files/libpng/libpng12/libpng-${pkgver}-apng.patch.gz")

prepare(){
  cd "${srcdir}/${_pkgbasename}-${pkgver}"

  # Add animated PNG (apng) support
  # see http://sourceforge.net/projects/libpng-apng/
  patch -Np0 -i "${srcdir}/libpng-${pkgver}-apng.patch"
}

build() {
  export CC="gcc -m32"
  export CXX="g++ -m32"
  export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"

  cd "${srcdir}/${_pkgbasename}-${pkgver}"

  libtoolize --force --copy
  aclocal
  autoconf
  automake --add-missing

  ./configure --prefix=/usr --libdir=/usr/lib32
  make
}

package() {
  cd "${srcdir}/${_pkgbasename}-${pkgver}"
  make DESTDIR="${pkgdir}" install

  rm -f ${pkgdir}/usr/lib32/{libpng.so,libpng.a,pkgconfig/libpng.pc}
  rm -rf ${pkgdir}/usr/{include,share,bin}

  mkdir -p "${pkgdir}/usr/share/licenses"
  install -D -m644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
}
sha256sums=('cf85516482780f2bc2c5b5073902f12b1519019d47bf473326c2018bdff1d272'
            '2c2f14464890360801ea3ad1b361f7dd7414ecfec26e3be4bb95934a6cc8cc0a')
