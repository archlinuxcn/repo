# Maintainer: Adam Fontenot <fontenot@ucla.edu>

pkgname=libheif
pkgver=1.1.0
pkgrel=1
pkgdesc="HEIF file format decoder and encoder"
arch=('i686' 'x86_64')
url="https://github.com/strukturag/libheif"
license=('GPL3')
depends=('libde265')
optdepends=('x265: HEIF encoding')
source=("$url/archive/v$pkgver.tar.gz")
sha256sums=('4ddeacbf1edc4c21e22266c66ccf5366ae4018bd9a02694f246883f3796ffbd2')

prepare() {
  cd "$pkgname-$pkgver"
}

build() {
  cd "$pkgname-$pkgver"
  ./autogen.sh
  ./configure --prefix=/usr --enable-static=no
  make
}

package() {
  cd "$pkgname-$pkgver"
  make DESTDIR="$pkgdir" install
}
