# Maintainer: Peter Lamby <peterlamby@web.de>
pkgname=libmpris2client
pkgver=0.1.0
pkgrel=1
pkgdesc="A glib library for controlling any mpris2 compatible player."
arch=('i686' 'x86_64')
url="https://github.com/matiasdelellis/libmpris2client"
license=('GPL2')
depends=('gtk2' 'glib2')
source=(https://github.com/matiasdelellis/$pkgname/releases/download/V$pkgver/$pkgname-$pkgver.tar.bz2)
md5sums=('854e641cf69c73cead92a4dfa760b0e4')

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  ./configure --prefix=/usr --sysconfdir=/etc --libexecdir=/lib 
  make
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"

  make DESTDIR="${pkgdir}" install
}
