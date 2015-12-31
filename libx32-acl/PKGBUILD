# $Id: PKGBUILD 98856 2013-10-20 15:20:08Z thomas $
# Maintainer: Thomas Bächler <thomas@archlinux.org>
# x32 Maintainer: Fantix King <fantix.king at gmail.com> 

pkgname=libx32-acl
pkgver=2.2.52
pkgrel=2.1
pkgdesc="Access control list libraries (x32 ABI)"
arch=('x86_64')
url="http://savannah.nongnu.org/projects/acl"
license=('LGPL')
depends=('libx32-attr>=2.4.46' 'acl')
makedepends=('gcc-multilib-x32')
source=(http://download.savannah.gnu.org/releases/acl/acl-${pkgver}.src.tar.gz)
sha256sums=('179074bb0580c06c4b4137be4c5a92a701583277967acdb5546043c7874e0d23')

build() {
  cd "${srcdir}/acl-${pkgver}"

  export CC="gcc -mx32"
  export PKG_CONFIG_PATH="/usr/libx32/pkgconfig"

  export INSTALL_USER=root INSTALL_GROUP=root 
  ./configure --prefix=/usr --libdir=/usr/libx32 --libexecdir=/usr/libx32
  make 
}

package() {
  cd "${srcdir}/acl-${pkgver}"

  make DIST_ROOT="${pkgdir}" install install-lib install-dev

  # tidy up
  rm -f ${pkgdir}/libx32/libacl.a
  chmod 0755 "$pkgdir"/usr/libx32/libacl.so.*.*.*

  rm -rf ${pkgdir}/usr/{bin,include,share}
}
