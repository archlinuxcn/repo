# Maintainer: Arthur Zamarin <arthurzam@gmail.com>
# Contributor:	dorphell			<archlinux.org: dorphell>
# Contributor:	Travis Willard			<archlinux.org: travis>
# Contributor:	Douglas Soares de Andrade	<archlinux.org: douglas>
# Contributor:	Jesse Jaara			<gmail.com: jesse.jaara>

pkgname=libpng12
_realname=libpng
pkgver=1.2.56
pkgrel=3
pkgdesc="A collection of routines used to create PNG format graphics files"
arch=('i686' 'x86_64' 'armv7h')
url="http://www.libpng.org/pub/png/libpng.html"
license=('custom')
depends=('zlib')
source=("http://sourceforge.net/projects/libpng/files/libpng12/${pkgver}/libpng-${pkgver}.tar.xz"
        "http://sourceforge.net/projects/libpng-apng/files/libpng12/${pkgver}/libpng-${pkgver}-apng.patch.gz")

sha256sums=('24ce54581468b937734a6ecc86f7e121bc46a90d76a0d948dca08f32ee000dbe'
            'b689af23e7c399b1f5d1fc0a7ed0540a5e678bcb665bc70f377d0569b278f3d9')
prepare() {
  cd "${srcdir}/${_realname}-${pkgver}"
  patch -Np1 -i "${srcdir}/libpng-${pkgver}-apng.patch"
}

build() {
  cd "${srcdir}/${_realname}-${pkgver}"

  # Removed bacause problems with automake system; Check in future updates
  #libtoolize --force --copy
  #aclocal
  #autoconf
  #automake --add-missing

  ./configure --prefix=/usr

  make ECHO=echo
}

package() {
  cd "${srcdir}/${_realname}-${pkgver}"

  make ECHO=echo DESTDIR="${pkgdir}" install

  rm -rf "${pkgdir}/usr/share"
  rm -rf "${pkgdir}/usr/bin/libpng-config"
  rm -rf "${pkgdir}/usr/lib/"{libpng.so,libpng.a}
  rm -fr "${pkgdir}/usr/lib/pkgconfig/libpng.pc"
  rm -rf "${pkgdir}/usr/include/"{pngconf.h,png.h}

  install -Dm644 LICENSE $pkgdir/usr/share/licenses/libpng12/LICENSE
}
