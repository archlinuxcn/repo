# $Id: PKGBUILD 92705 2013-06-12 16:03:23Z lcarlier $
# Maintainer: Thomas Bächler <thomas@archlinux.org>
# x32 Maintainer: Fantix King <fantix.king at gmail.com>

_pkgbasename=attr
pkgname=libx32-$_pkgbasename
pkgver=2.4.47
pkgrel=1.1
pkgdesc="Extended attribute support library for ACL support (x32 ABI)"
arch=(x86_64)
url="http://savannah.nongnu.org/projects/attr"
license=('LGPL')
depends=('libx32-glibc' $_pkgbasename)
makedepends=('gcc-multilib-x32' 'gettext')
options=('!libtool')
source=(http://download.savannah.gnu.org/releases/attr/attr-${pkgver}.src.tar.gz)
sha256sums=('25772f653ac5b2e3ceeb89df50e4688891e21f723c460636548971652af0a859')

build() {
  cd ${srcdir}/attr-${pkgver} 

  export CC="gcc -mx32"
  export PKG_CONFIG_PATH="/usr/libx32/pkgconfig"

  export INSTALL_USER=root INSTALL_GROUP=root
  ./configure --prefix=/usr --libdir=/usr/libx32 --libexecdir=/usr/libx32
  make 
}

package() {
  cd ${srcdir}/attr-${pkgver} 

  make DIST_ROOT="${pkgdir}" install-lib install-dev

  # tidy up
  rm -f "$pkgdir"/usr/libx32/libattr.a
  chmod 0755 "$pkgdir"/usr/libx32/libattr.so.*.*.*

  rm -rf "${pkgdir}"/usr/{bin,include,share}
}
