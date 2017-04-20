# Maintainer: Colin Keenan <colinnkeenan at gmail dot com>

pkgname=silentcast
pkgver=3.04
pkgrel=1
pkgdesc="Silent Screencast: video record your screen and make it into an animated gif"
arch=('x86_64')
url="https://github.com/colinkeenan/silentcast"
license=('GPL3')
depends=('ffmpeg' 'imagemagick' 'gtk3')

source=($url"/archive/v"$pkgver".tar.gz")
md5sums=('19c16ffd876c2e1189f841b46f662dd5')

package() {
  cd "$pkgname-$pkgver"
  make
  ./install "$pkgdir/"
}
