# Maintainer: vimacs <https://vimacs.lcpu.club>

pkgname=mypaint-brushes
pkgver=1.3.0
pkgrel=1
pkgdesc='Brushes used by MyPaint and other software using libmypaint.'
arch=('any')
url='https://github.com/Jehan/mypaint-brushes'
license=('CC0')
depends=('libmypaint=1.3.0')
source=("https://github.com/Jehan/mypaint-brushes/archive/v${pkgver}.tar.gz")
sha256sums=('704bb6420e65085acfd7a61d6050e96b0395c5eab078433f11406c355f16b214')

build() {
  cd "$pkgname-$pkgver"

  ./autogen.sh
  ./configure --prefix=/usr
  make
}

package() {
  cd "$pkgname-$pkgver"

  make DESTDIR="$pkgdir" install
  install -D -m644 COPYING "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
