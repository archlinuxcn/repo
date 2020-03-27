# Maintainer: WorMzy Tykashi <wormzy.tykashi@gmail.com>
# Contributor: FadeMind <fademind@gmail.com>
# Contributor: Richard Jackson <rj@iinet.net.au>
pkgname=abiword-gtk2
_pkgname=abiword
pkgver=3.0.4
pkgrel=1
pkgdesc='Fully-featured word processor, GTk2, No plugins, Lite version'
arch=('i686' 'x86_64')
license=('GPL')
depends=('fribidi' 'wv' 'librsvg' 'enchant' 'desktop-file-utils' 'gtk2' 'libxslt')
makedepends=('boost')
conflicts=('abiword' 'abiword-plugins')
url='http://www.abisource.com'
source=("$_pkgname-$pkgver.tar.gz::http://abisource.com/downloads/$_pkgname/$pkgver/source/$_pkgname-$pkgver.tar.gz"
        enchant-2.patch)
sha256sums=('e93096cb192e5bc19d62e180fc5eda643206465315a710113ae5036bc2a1a5d7'
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
