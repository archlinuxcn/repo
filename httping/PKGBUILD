# Maintainer: brent s. <bts[at]square-r00t[dot]net>
# Past maintainer: Joris Steyn <jorissteyn@gmail.com>
# Contributor: Ondrej Kucera <ondrej.kucera@centrum.cz>

pkgname=httping
pkgver=2.4
pkgrel=1
pkgdesc="A 'ping'-like tool for http-requests"
arch=(i686 x86_64)
depends=("openssl")
optdepends=("ncurses"
            "fftw")
url=('http://www.vanheusden.com/httping/')
license=('GPL')
source=("http://www.vanheusden.com/httping/${pkgname}-${pkgver}.tgz")
md5sums=('3b4d003276c1346c32629b65262dfd1e')

build() {
  cd ${srcdir}/${pkgname}-${pkgver}
  make 
}

package() {
  cd ${srcdir}/${pkgname}-${pkgver}
  mkdir -p ${pkgdir}/usr/bin
  mkdir -p ${pkgdir}/usr/share/man/nl/man1
  mkdir -p ${pkgdir}/usr/share/locale/nl/LC_MESSAGES/
  make DESTDIR=${pkgdir} install
}
