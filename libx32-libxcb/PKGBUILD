# $Id: PKGBUILD 116722 2014-08-02 03:14:37Z lcarlier $
# Maintainer: Alexander Baldeck <alexander@archlinux.org>
# Contributor: Jan de Groot <jgc@archlinux.org>
# x32 Maintainer: Fantix King <fantix.king at gmail.com>

_pkgbasename=libxcb
pkgname=libx32-$_pkgbasename
pkgver=1.11
pkgrel=1.1
pkgdesc="X11 client-side library (x32 ABI)"
arch=(x86_64)
url="http://xcb.freedesktop.org/"
depends=('libx32-libxdmcp' 'libx32-libxau' $_pkgbasename)
makedepends=('pkgconfig' 'libx32-libxslt' 'python' 'xorg-util-macros' 'gcc-multilib-x32'
             'autoconf')
license=('custom')
source=(${url}/dist/${_pkgbasename}-${pkgver}.tar.bz2
        libxcb-1.1-no-pthread-stubs.patch)
sha256sums=('03635d70045b9ede90778e67516135828a57de87ac508f987024f43c03620ff7'
	    '3923bcb1930b851012968435909597d8d5251c72153511cb2982636c97100cc3')

prepare() {
  cd "${srcdir}/${_pkgbasename}-${pkgver}"

  patch -Np1 -i "${srcdir}/libxcb-1.1-no-pthread-stubs.patch"
  autoreconf -vfi
}

build() {
  cd "${srcdir}/${_pkgbasename}-${pkgver}"

  export CC="gcc -mx32"
  export PKG_CONFIG_PATH="/usr/libx32/pkgconfig"

  ./autogen.sh \
	  --prefix=/usr \
	  --enable-xinput \
          --enable-xkb \
	  --libdir=/usr/libx32 \
	  --disable-static
  make
}

package() {
  cd "${srcdir}/${_pkgbasename}-${pkgver}"

  make DESTDIR="${pkgdir}" install

  rm -rf "${pkgdir}"/usr/{include,share}

  mkdir -p "$pkgdir/usr/share/licenses"
  ln -s $_pkgbasename "$pkgdir/usr/share/licenses/$pkgname" 
}
