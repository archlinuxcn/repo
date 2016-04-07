# Maintainer: brent s. <bts[at]square-r00t[dot]net>
validpgpkeys=('748231EBCBD808A14F5E85D28C004C2F93481F6B')
# Past maintainer: Joris Steyn <jorissteyn@gmail.com>
# Contributor: Ondrej Kucera <ondrej.kucera@centrum.cz>

pkgname=httping
pkgver=2.4
pkgrel=3
pkgdesc="A 'ping'-like tool for http-requests"
arch=(i686 x86_64)
depends=("openssl")
optdepends=("ncurses"
            "fftw")
url='http://www.vanheusden.com/httping/'
license=('GPL')
source=("http://www.vanheusden.com/httping/${pkgname}-${pkgver}.tgz"
	"${pkgname}-${pkgver}.tgz.sig")
sha512sums=('11d9e9e3b222548c9754cc0e7bf947f1a55ccc9f1a2401681f95d21b7b7a56c07665955b558a56d07a5c98497ea3644758e4f85006c42fda2134556be8d9e804'
            'SKIP')

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
