# Maintainer: Peter Lamby <peterlamby@web.de>
pkgname=deadbeef-mpris2-plugin
pkgver=1.11
pkgrel=1
pkgdesc="MPRISv2 plugin for the DeaDBeeF music player"
arch=('i686' 'x86_64')
url="https://github.com/Serranya/deadbeef-mpris2-plugin"
license=('GPL2')
depends=('glib2' 'deadbeef' )
conflicts=('deadbeef-mpris-plugin')
options=('!libtool')
source=(https://github.com/Serranya/$pkgname/releases/download/v$pkgver/$pkgname-$pkgver.tar.xz)
md5sums=('03923767ea3d5e7fc8ddd8c4af93b311')

build() {
  cd "${srcdir}/deadbeef-${pkgver}"
  ./configure --prefix=/usr 
  make
}

package() {
  cd "${srcdir}/deadbeef-${pkgver}"

  make DESTDIR="${pkgdir}" install
}
