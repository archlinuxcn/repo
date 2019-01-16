# Maintainer: Colin Keenan <colinnkeenan at gmail dot com>

pkgname=silentcast
pkgver=3.07
pkgrel=1
pkgdesc="Silent Screencast: video record your screen and make it into an animated gif"
arch=('x86_64')
url="https://github.com/colinkeenan/silentcast"
license=('GPL3')
depends=('ffmpeg' 'imagemagick' 'gtk3')

source=($url"/archive/v"$pkgver".tar.gz")
md5sums=('983b867f901132e2b83e4f7d28b64403')

package() {
  cd "$pkgname-$pkgver"
  make
  ./install "$pkgdir/"
}
