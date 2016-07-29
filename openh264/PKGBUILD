# Maintainer: drakkan <nicola.murino@gmail.com>
# Contributor: drakkan <nicola.murino@gmail.com>

pkgname=openh264
pkgver=1.6.0
pkgrel=1
pkgdesc='OpenH264 is a codec library which supports H.264 encoding and decoding'
license=('BSD')
arch=('x86_64' 'i686')
url="http://www.openh264.org/"
depends=('gcc-libs')
makedepends=('nasm')
source=("https://github.com/cisco/openh264/archive/v${pkgver}.tar.gz")
sha256sums=('65d307bf312543ad6e98ec02abb7c27d8fd2c9740fd069d7249844612674a2c7')

prepare() {
  cd "openh264-$pkgver"
  sed -i 's/PREFIX=\/usr\/local/PREFIX=\/usr/g' Makefile
}

build() {
  cd "openh264-$pkgver"
  make 
}

package() {
  cd "openh264-$pkgver"
  make DESTDIR="$pkgdir" install
  install -Dm755 h264dec "$pkgdir"/usr/bin/h264dec
  install -Dm755 h264enc "$pkgdir"/usr/bin/h264enc
  install -Dm644 LICENSE "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}

# vim:set ts=2 sw=2 et:
