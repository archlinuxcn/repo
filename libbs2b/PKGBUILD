# Maintainer: Gustavo Alvarez <sl1pkn07@gmail.com>
# Contributor: Panagiotis Papadopoulos pano_90 AT gmx DOT net 

pkgname=libbs2b
pkgver=3.1.0
pkgrel=5
pkgdesc="Bauer stereophonic-to-binaural DSP effect library"
arch=('i686' 'x86_64')
url='http://bs2b.sourceforge.net'
license=('MIT')
depends=('libsndfile')
source=(http://downloads.sourceforge.net/bs2b/$pkgname-$pkgver.tar.gz)
sha256sums=('6aaafd81aae3898ee40148dd1349aab348db9bfae9767d0e66e0b07ddd4b2528')

build() {
  cd "${pkgname}-${pkgver}"
  ./configure \
    --prefix=/usr

  make
}

package() {
  cd "${pkgname}-${pkgver}"
  make DESTDIR="${pkgdir}" install

  install -Dm644 COPYING "${pkgdir}/usr/share/licenses/${pkgname}/COPYING"
}
