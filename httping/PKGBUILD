# Maintainer: Joris Steyn <jorissteyn@gmail.com>
# Contributor: Ondrej Kucera <ondrej.kucera@centrum.cz>

pkgname=httping
pkgver=2.3.4
pkgrel=1
pkgdesc="A 'ping'-like tool for http-requests"
arch=(i686 x86_64)
depends=("openssl")
optdepends=("ncurses"
            "fftw")
url=('http://www.vanheusden.com/httping/')
license=('GPL')
source=("http://www.vanheusden.com/httping/${pkgname}-${pkgver}.tgz")
md5sums=('7a71ed513f9f22fe331b783a3d36767e')

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
