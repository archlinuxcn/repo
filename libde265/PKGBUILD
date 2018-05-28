# Maintainer: James An <james@jamesan.ca>
# Contributor: Daniel Nagy <danielnagy at gmx de>

pkgname=libde265
pkgver=1.0.2
pkgrel=3
pkgdesc="Open h.265 video codec implementation"
arch=('i686' 'x86_64')
url="https://github.com/strukturag/libde265"
license=('LGPL3')
depends=('gcc-libs')
optdepends=('ffmpeg: for sherlock265'
            'qt5-base: for sherlock265'
            'sdl: dec265 YUV overlay output')
source=("$url/archive/v$pkgver.tar.gz")
md5sums=('7c7f97db66b562d9866ae8e86d6ea3e7')

prepare() {
  cd "$pkgname-$pkgver"
  sed -ri 's/(PIX_FMT_)/AV_\1/g' sherlock265/VideoDecoder.cc
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
