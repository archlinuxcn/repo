# Maintainer: Natrio <natrio list ru>
# Contributor: Thayer Williams <thayer archlinux org>
# Contributor: Douglas Soares de Andrade <douglas archlinux org>
# Contributor: Robson Peixoto

pkgname=unzip-natspec
pkgver=6.0
pkgrel=5
pkgdesc="Unpacks .zip archives with non-latin filenames, using libnatspec patch from AltLinux."
arch=('i686' 'x86_64' 'armv7h' 'armv6h')
url="http://www.info-zip.org/"
license=('custom')
depends=('bzip2' 'bash' 'libnatspec')
conflicts=('unzip')
provides=('unzip')
source=('http://downloads.sourceforge.net/infozip/unzip60.tar.gz' 
 unzip-6.0-alt-natspec.patch
 test_compr_eb.patch getZip64Data.patch crc32.patch )
sha256sums=('036d96991646d0449ed0aa952e4fbe21b476ce994abc276e49d30e686708bd37'
 SKIP SKIP SKIP SKIP )

build() {
  cd ${srcdir}/${pkgname/-natspec/}${pkgver/./}
  patch -p1 -i ${srcdir}/unzip-6.0-alt-natspec.patch || return 1
  patch -i ${srcdir}/test_compr_eb.patch || return 1 # FS#43391
  patch -i ${srcdir}/getZip64Data.patch || return 1 # FS#43300
  patch -i ${srcdir}/crc32.patch || return 1 # FS#43300
  export CFLAGS="$CFLAGS -D_FILE_OFFSET_BITS=64 -DACORN_FTYPE_NFS \
  -DWILD_STOP_AT_DIR -DLARGE_FILE_SUPPORT -DUNICODE_SUPPORT \
  -DUNICODE_WCHAR -DUTF8_MAYBE_NATIVE -DNO_LCHMOD -DDATE_FORMAT=DF_YMD \
  -DUSE_BZIP2 -DNATIVE -DNOMEMCPY -DNO_SETLOCALE"
  make -f unix/Makefile LOCAL_UNZIP="$CFLAGS" prefix=/usr \
  D_USE_BZ2=-DUSE_BZIP2 L_BZ2=-lbz2 unzips || return 1
}

package() {
  cd ${srcdir}/${pkgname/-natspec/}${pkgver/./}
  make -f unix/Makefile prefix=$pkgdir/usr INSTALL_PROGRAM="install" install || return 1
  install -Dm644 LICENSE $pkgdir/usr/share/licenses/unzip/LICENSE || return 1
  mkdir -p $pkgdir/usr/share || return 1
  mv $pkgdir/usr/man $pkgdir/usr/share/ || return 1
}
