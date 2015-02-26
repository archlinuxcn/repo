# $Id: PKGBUILD 123858 2014-12-13 21:59:05Z thestinger $
# Maintainer: Jan de Groot <jgc@archlinux.org>
# x32 Maintainer: Fantix King <fantix.king at gmail.com>

pkgname=libx32-libffi
pkgver=3.2.1
pkgrel=1.1
pkgdesc="A portable, high level programming interface to various calling conventions (x32 ABI)"
arch=('x86_64')
license=('MIT')
url="http://sourceware.org/libffi/"
depends=('libx32-glibc')
checkdepends=('dejagnu')
source=(ftp://sourceware.org/pub/libffi/libffi-${pkgver}.tar.gz)
sha1sums=('280c265b789e041c02e5c97815793dfc283fb1e6')

build() {
  cd libffi-${pkgver}

  export CC="gcc -mx32"

  ./configure --prefix=/usr \
    --libdir=/usr/libx32 --libexecdir=/usr/libx32 \
    --disable-static --enable-pax_emutramp \
    --host=x86_64-unknown-linux-gnux32

  make
}

check() {
  make -C libffi-${pkgver} check
}

package() {
  cd libffi-${pkgver}

  make DESTDIR="${pkgdir}" install

  install -m755 -d "${pkgdir}/usr/share/licenses/${pkgname}"
  install -m644 LICENSE "${pkgdir}/usr/share/licenses/${pkgname}/"
  rm -r "${pkgdir}"/usr/share/{info,man}
}
