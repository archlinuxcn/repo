# Maintainer: Gustavo Alvarez <sl1pkn07@gmail.com>
# Contributor: Panagiotis Papadopoulos pano_90 AT gmx DOT net 

pkgname=libbs2b
pkgver=3.1.0
pkgrel=4
pkgdesc="Bauer stereophonic-to-binaural DSP effect library"
arch=('i686' 'x86_64')
url='http://bs2b.sourceforge.net'
license=('GPL')
depends=('libsndfile')
source=(http://downloads.sourceforge.net/bs2b/$pkgname-$pkgver.tar.gz)
sha1sums=('a71318211611a00bd3d595b0830d2188938ff89d')

build() {
  cd "${pkgname}-${pkgver}"
  ./configure --prefix=/usr
  make
}

package() {
  cd "${pkgname}-${pkgver}"
  make DESTDIR="${pkgdir}" install
}
