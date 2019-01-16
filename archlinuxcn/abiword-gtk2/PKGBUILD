# Maintainer: WorMzy Tykashi <wormzy.tykashi@gmail.com>
# Contributor: FadeMind <fademind@gmail.com>
# Contributor: Richard Jackson <rj@iinet.net.au>
pkgname=abiword-gtk2
_pkgname=abiword
pkgver=3.0.2
pkgrel=3
pkgdesc='Fully-featured word processor, GTk2, No plugins, Lite version'
arch=('i686' 'x86_64')
license=('GPL')
depends=('fribidi' 'wv' 'librsvg' 'enchant' 'desktop-file-utils' 'gtk2' 'libxslt')
makedepends=('pkgconfig' 'boost')
conflicts=('abiword' 'abiword-plugins')
url='http://www.abisource.com'
source=("$_pkgname-$pkgver.tar.gz::http://abisource.com/downloads/$_pkgname/$pkgver/source/$_pkgname-$pkgver.tar.gz"
        enchant-2.patch)
sha256sums=('afbfd458fd02989d8b0c6362ba8a4c14686d89666f54cfdb5501bd2090cf3522'
            'f510f4df2cf597f5493f52ce855b4209628d7622b03532c2ef221f8b7032a349')

prepare() {
  cd $_pkgname-$pkgver

  # Replace deprecated enchant functions
  patch -Np1 -i ../enchant-2.patch
}

build() {
  cd $_pkgname-$pkgver

  ./configure --prefix=/usr \
    --enable-shared \
    --disable-static \
    --with-gtk2 \
    --enable-clipart \
    --enable-templates \
    --enable-spell \
    --without-redland \
    --without-libical \
    --disable-builtin-plugins \
    --disable-default-plugins \
    --disable-collab-backend-service \
    --disable-collab-backend-tcp
  make -C goffice-bits2
  make
}

package() {
  cd $_pkgname-$pkgver
  make DESTDIR="$pkgdir" install
}
