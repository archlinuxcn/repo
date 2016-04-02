# Maintainer: Arthur Zamarin <arthurzam@gmail.com>
# Contributor: trya <tryagainprod@gmail.com>
# Contributor: Jan de Groot <jgc@archlinux.org>
# Contributor: dorphell <dorphell@archlinux.org>
# Contributor: Travis Willard <travis@archlinux.org>
# Contributor: Douglas Soares de Andrade <douglas@archlinux.org>

_pkgbasename=libpng
pkgname=lib32-libpng12
pkgver=1.2.56
pkgrel=2
pkgdesc="A collection of routines used to create PNG format graphics files (32-bit, 1.2 branch)"
arch=('x86_64')
url="http://www.libpng.org/pub/png/libpng.html"
license=('custom')
depends=('lib32-zlib' 'libpng12')
makedepends=('gcc-multilib') 
options=('!libtool')
source=("http://sourceforge.net/projects/libpng/files/libpng12/${pkgver}/libpng-${pkgver}.tar.xz"
        "http://sourceforge.net/projects/libpng-apng/files/libpng12/${pkgver}/libpng-${pkgver}-apng.patch.gz")

prepare(){
  cd "${srcdir}/${_pkgbasename}-${pkgver}"

  # Add animated PNG (apng) support
  # see http://sourceforge.net/projects/libpng-apng/
  patch -Np1 -i "${srcdir}/libpng-${pkgver}-apng.patch"
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
sha256sums=('24ce54581468b937734a6ecc86f7e121bc46a90d76a0d948dca08f32ee000dbe'
            'b689af23e7c399b1f5d1fc0a7ed0540a5e678bcb665bc70f377d0569b278f3d9')
