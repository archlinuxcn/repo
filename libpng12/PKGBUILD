# Maintainer: Arthur Zamarin <arthurzam@gmail.com>
# Contributor:	dorphell			<archlinux.org: dorphell>
# Contributor:	Travis Willard			<archlinux.org: travis>
# Contributor:	Douglas Soares de Andrade	<archlinux.org: douglas>
# Contributor:	Jesse Jaara			<gmail.com: jesse.jaara>

pkgname=libpng12
_realname=libpng
pkgver=1.2.53
pkgrel=2
pkgdesc="A collection of routines used to create PNG format graphics files"
arch=('i686' 'x86_64' 'armv7h')
url="http://www.libpng.org/pub/png/libpng.html"
license=('custom')
depends=('zlib')
source=("http://sourceforge.net/projects/libpng/files/libpng12/${pkgver}/libpng-${pkgver}.tar.xz"
        "http://sourceforge.net/projects/apng/files/libpng/libpng12/libpng-${pkgver}-apng.patch.gz")

build() {
  cd "${srcdir}/${_realname}-${pkgver}"

  patch -Np0 -i "${srcdir}/libpng-${pkgver}-apng.patch"

  libtoolize --force --copy
  aclocal
  autoconf
  automake --add-missing

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

sha256sums=('b45e49f689e7451bd576569e6a344f7e0d11c02ecbb797f4da0e431526765c0a'
            '64745f978fd9419a533942181316ddd1cafce63e899bc572f37d6614831c8ed3')
