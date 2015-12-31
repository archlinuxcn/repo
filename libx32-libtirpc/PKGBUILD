# $Id: PKGBUILD 146918 2015-11-16 10:34:48Z alucryd $
# Maintainer: Maxime Gauduin <alucryd@archlinux.org>
# Contributor: jtts <jussaar@mbnet.fi>
# Contributor: Tom Gundersen <teg@jklm.no>
# Contributor: Tobias Powalowski <tpowa@archlinux.org>
# Contributor: Franco Tortoriello <franco.tortoriello@gmail.com>
# Contributor: josephgbr <rafael.f.f1@gmail.com>
# x32 Maintainer: Fantix King <fantix.king at gmail.com>

pkgname=libx32-libtirpc
pkgver=1.0.1
pkgrel=1.1
pkgdesc='Transport Independent RPC library (SunRPC replacement) (x32 ABI)'
arch=('x86_64')
url='http://libtirpc.sourceforge.net/'
license=('BSD')
depends=('libx32-krb5' 'libtirpc')
makedepends=('gcc-multilib-x32')
source=("http://downloads.sourceforge.net/sourceforge/libtirpc/libtirpc-${pkgver}.tar.bz2"
        'add_missing_rwlock_unlocks_in_xprt_register.diff')
sha256sums=('5156974f31be7ccbc8ab1de37c4739af6d9d42c87b1d5caf4835dda75fcbb89e'
            '8bcdbd700ec6f8b5f87881251f9851174df233975d95a8dfdf7359f057fb3b80')

prepare() {
  cd libtirpc-${pkgver}

  patch -Np1 -i ../add_missing_rwlock_unlocks_in_xprt_register.diff
}

build() {
  cd libtirpc-${pkgver}

  export CC='gcc -mx32'
  export CXX='g++ -mx32'
  export PKG_CONFIG_PATH='/usr/libx32/pkgconfig'

  ./configure \
    --prefix='/usr' \
    --libdir='/usr/libx32' \
    --sysconfdir='/etc'
  make
}

package() {
  cd libtirpc-${pkgver}

  make DESTDIR="${pkgdir}" install
  rm -rf "${pkgdir}"/{etc,usr/{include,share}}

  install -dm 755 "${pkgdir}"/usr/share/licenses
  ln -s libtirpc "${pkgdir}"/usr/share/licenses/${pkgname}
}

# vim: ts=2 sw=2 et:
