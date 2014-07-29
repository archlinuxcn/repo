# $Id: PKGBUILD 115638 2014-07-13 07:05:40Z lcarlier $
# Maintainer: Alexander Baldeck <alexander@archlinux.org>
# Contributor: Jan de Groot <jgc@archlinux.org>
# x32 Maintainer: Fantix King <fantix.king at gmail.com>

_pkgbasename=libxcb
pkgname=libx32-$_pkgbasename
pkgver=1.10
pkgrel=3
pkgdesc="X11 client-side library (x32 ABI)"
arch=(x86_64)
url="http://xcb.freedesktop.org/"
depends=('libx32-libxdmcp' 'libx32-libxau' $_pkgbasename)
makedepends=('pkgconfig' 'libx32-libxslt' 'python' 'gcc-multilib-x32'
             'autoconf')
license=('custom')
source=(${url}/dist/${_pkgbasename}-${pkgver}.tar.bz2
        libxcb-1.1-no-pthread-stubs.patch
	Ensure-xcb-owns-socket-and-no-other-threads-are-writ.patch
        Force-XCB-event-structures-with-64-bit-extended-fiel.patch)
sha256sums=('98d9ab05b636dd088603b64229dd1ab2d2cc02ab807892e107d674f9c3f2d5b5'
            '748ed83af60468a0eb6785222e4a5ca589d28f20b9bfc60d5936ec93b8eef356'
	    '47de1025bb16446b9e69ff7b6b262a0a1af957d350afe897421b9105c89befeb'
            '7dd84c631da541e2dc708323071c3306ceaf79ee807aa457c1cdc7e069b7ccb9')

prepare() {
  cd "${srcdir}/${_pkgbasename}-${pkgver}"

  patch -Np1 -i "${srcdir}/libxcb-1.1-no-pthread-stubs.patch"
  autoreconf -vfi

  # fix FS#40289 merged upstream 
  patch -Np1 -i ../Ensure-xcb-owns-socket-and-no-other-threads-are-writ.patch 
  # fix FS#41172 merged upstream
  patch -Np1 -i ../Force-XCB-event-structures-with-64-bit-extended-fiel.patch
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
