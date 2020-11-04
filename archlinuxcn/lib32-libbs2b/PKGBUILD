# Maintainer: Gustavo Alvarez <sl1pkn07@gmail.com>
# Contributor: Panagiotis Papadopoulos pano_90 AT gmx DOT net 
pkgname=lib32-libbs2b
_pkgname=libbs2b
pkgver=3.1.0
pkgrel=3
pkgdesc="Bauer stereophonic-to-binaural DSP effect library"
arch=('i686' 'x86_64')
url='http://bs2b.sourceforge.net'
license=('GPL')
depends=('lib32-libsndfile' 'libbs2b')
source=(https://cfhcable.dl.sourceforge.net/project/bs2b/$_pkgname/$pkgver/$_pkgname-$pkgver.tar.gz)
sha1sums=('a71318211611a00bd3d595b0830d2188938ff89d')

build() {
  cd "${_pkgname}-${pkgver}"
  export CC="gcc -m32"
  export CXX="g++ -m32"
  export PKG_CONFIG_PATH='/usr/lib32/pkgconfig'
  ./configure --prefix=/usr --libdir=/usr/lib32
  make
}

package() {
  cd "${_pkgname}-${pkgver}"
  make DESTDIR="${pkgdir}" install
  rm -rf $pkgdir/usr/{include,bin}
}
