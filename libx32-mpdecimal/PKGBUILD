# $Id: PKGBUILD 221617 2014-09-13 11:13:02Z fyan $
# Maintainer: Felix Yan <felixonmars@gmail.com>
# x32 Maintainer: Fantix King <fantix.king@gmail.com>

_basepkgname=mpdecimal
pkgname=libx32-$_basepkgname
pkgver=2.4.1
pkgrel=1.2
pkgdesc="Package for correctly-rounded arbitrary precision decimal floating point arithmetic (x32 ABI)"
arch=('i686' 'x86_64')
url="http://www.bytereef.org/mpdecimal/index.html"
license=('custom')
depends=('libx32-glibc' $_basepkgname)
source=(http://www.bytereef.org/software/${_basepkgname}/releases/${_basepkgname}-${pkgver}.tar.gz
        'mpdecimal-stub.h')

build() {
  cd ${_basepkgname}-${pkgver}

  export CC="gcc -mx32"
  export CXX="g++ -mx32"
  export PKG_CONFIG_PATH="/usr/libx32/pkgconfig"

  ./configure --prefix=/usr --libdir=/usr/libx32
  make
}

package() {
  install="${pkgname}.install"

  cd ${_basepkgname}-${pkgver}
  make DESTDIR="${pkgdir}" install

  mv "${pkgdir}/usr/include/mpdecimal.h" "${srcdir}/mpdecimal-x32.h"
  rm -rf "${pkgdir}"/usr/share
  install -Dm644 "${srcdir}/mpdecimal-x32.h" "${pkgdir}/usr/include/mpdecimal-x32.h"
  install -Dm644 "${srcdir}/mpdecimal-stub.h" "${pkgdir}/usr/include/mpdecimal-stub.h"

  mkdir -p "$pkgdir/usr/share/licenses"
  ln -s $_basepkgname "$pkgdir/usr/share/licenses/$pkgname"
}

sha512sums=('60073ec82faff1ef9a5955a98f7f1320b044ff03bf8589bfe139b4721ae44c943e16bb36e1e61d9c6016529ba460d879bcbb17ea17cd875b27caa7caea211d45'
            'c2a271daf129be4b2bb538c76add6491a59ff47b3c927cafaa2ba9440a1f2dbdb9670284188c051a2c0470184a560244d458b0d46b6f8e95b65114774a06114d')
