# Maintainer: drakkan <nicola.murino at gmail dot com>
# Contributor: drakkan <nicola.murino at gmail dot com>

pkgname=openh264
pkgver=2.2.0
pkgrel=2
pkgdesc='OpenH264 is a codec library which supports H.264 encoding and decoding'
license=('BSD')
arch=('x86_64' 'i686' 'aarch64')
url="http://www.openh264.org/"
depends=('gcc-libs')
makedepends=('nasm')
provides=('libopenh264.so')
source=("https://github.com/cisco/openh264/archive/v${pkgver}.tar.gz")
sha256sums=('e4e5c8ba48e64ba6ce61e8b6e2b76b2d870c74c270147649082feabb40f25905')

build() {
  cd "openh264-$pkgver"
  make 
}

package() {
  cd "openh264-$pkgver"
  make DESTDIR="$pkgdir" PREFIX="/usr" install
  install -Dm755 h264dec "$pkgdir"/usr/bin/h264dec
  install -Dm755 h264enc "$pkgdir"/usr/bin/h264enc
  install -Dm644 LICENSE "$pkgdir"/usr/share/licenses/$pkgname/LICENSE
}

# vim:set ts=2 sw=2 et:
