# Maintainer: twa022 <twa022 at gmail dot com>

pkgname=libmypaint
pkgver=1.3.0
pkgrel=3
pkgdesc="a library for making brushstrokes which is used by MyPaint and other projects, with GEGL support"
arch=('i686' 'x86_64')
url="http://mypaint.org/"
license=('ISC')
depends=('json-c>=0.13' 'gegl')
makedepends=('intltool' 'python' 'gobject-introspection')
source=("$pkgname-$pkgver.tar.gz::https://github.com/mypaint/libmypaint/archive/v${pkgver}.tar.gz"
        'versioning.patch')
sha256sums=('8fbdce62f66a027d8b43fa8b061f0e6ff2a3da63cbe55a82d1642e5e39da0654'
            'd850f9b64bc037bd7ed6bbcec0a39115dd43ff896aef59daea79d8786fbb28c0')

prepare() {
  cd "$pkgname-$pkgver"

  patch -uNp2 -r- -i ../versioning.patch
}

build() {
  cd "$pkgname-$pkgver"

  ./autogen.sh
  ./configure --prefix=/usr --enable-gegl
  make
}

package() {
  cd "$pkgname-$pkgver"

  make DESTDIR="$pkgdir" install
  install -D -m644 COPYING "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
