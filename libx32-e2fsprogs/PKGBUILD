# $Id: PKGBUILD 119148 2014-09-18 03:10:07Z fyan $
# Maintainer:  Ionut Biru <ibiru@archlinux.org>
# Contributor: mightyjaym <jm.ambrosino@free.fr>
# Contributor: Mikko Seppälä <t-r-a-y@mbnet.fi>
# x32 Maintainer: Fantix King <fantix.king at gmail.com>

_pkgbasename=e2fsprogs
pkgname=libx32-e2fsprogs
pkgver=1.42.12
pkgrel=1.1
pkgdesc="Ext2 filesystem libraries (x32 ABI)"
arch=('x86_64')
license=('GPL' 'LGPL' 'MIT')
url="http://e2fsprogs.sourceforge.net"
depends=('libx32-util-linux' $_pkgbasename)
makedepends=('bc' 'gcc-multilib-x32')
source=(
    "http://downloads.sourceforge.net/sourceforge/${_pkgbasename}/${_pkgbasename}-${pkgver}.tar.gz"
    'ext2_types-stub.h'
)
sha1sums=('083c1bb0d1e85672e8038a2fadf70b24e7409db7'
          'c8b86107cea7f508d6dfd16313e4b511b8fc701a')

build() {
  export CC="gcc -mx32"
  export CXX="g++ -mx32"
  export PKG_CONFIG_PATH="/usr/libx32/pkgconfig"

  cd "${srcdir}/${_pkgbasename}-${pkgver}"
  ./configure --prefix=/usr --libdir=/usr/libx32 --with-root-prefix="" --enable-elf-shlibs \
      --disable-{debugfs,imager,resizer,fsck,uuidd,libuuid,libblkid}
  make
}

package() {
  install="${pkgname}.install"

  cd "${srcdir}/${_pkgbasename}-${pkgver}"
  make DESTDIR="${pkgdir}" install-libs

  mv "${pkgdir}/usr/include/ext2fs/ext2_types.h" "${srcdir}/ext2_types.h"
  rm -rf "${pkgdir}"/usr/{bin,include,share}
  install -Dm644 "${srcdir}/ext2_types.h" "${pkgdir}/usr/include/ext2fs/ext2_types-x32.h"
  install -Dm644 "${srcdir}/ext2_types-stub.h" "${pkgdir}/usr/include/ext2fs/ext2_types-stub.h"
  mkdir -p "$pkgdir/usr/share/licenses"
  ln -s $_pkgbasename "$pkgdir/usr/share/licenses/$pkgname"
}
