# $Id: PKGBUILD 113590 2014-06-26 09:15:49Z lcarlier $
# Maintainer: Jan de Groot <jgc@archlinux.org>
# x32 Maintainer: Fantix King <fantix.king at gmail.com>

pkgname=libx32-libffi
pkgver=3.1
pkgrel=1
pkgdesc="A portable, high level programming interface to various calling conventions (x32 ABI)"
arch=('x86_64')
license=('MIT')
url="http://sourceware.org/libffi/"
depends=('libx32-glibc')
checkdepends=('dejagnu')
source=(ftp://sourceware.org/pub/libffi/libffi-${pkgver}.tar.gz
        0001-Fix-paths-in-libffi.pc.in.patch)
sha1sums=('cb373ef2115ec7c57913b84ca72eee14b10ccdc3'
          '85b406c5208a7b8fdba9c8a4782ab524f5c5eec4')

prepare() {
  cd libffi-${pkgver}
  patch -p1 -i ../0001-Fix-paths-in-libffi.pc.in.patch
}

build() {
  cd libffi-${pkgver}

  export CC="gcc -mx32"

  ./configure --prefix=/usr \
    --libdir=/usr/libx32 --libexecdir=/usr/libx32 \
    --disable-static --host=x86_64-unknown-linux-gnux32

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
