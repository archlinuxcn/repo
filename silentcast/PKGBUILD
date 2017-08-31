# Maintainer: Colin Keenan <colinnkeenan at gmail dot com>

pkgname=silentcast
pkgver=3.06
pkgrel=1
pkgdesc="Silent Screencast: video record your screen and make it into an animated gif"
arch=('x86_64')
url="https://github.com/colinkeenan/silentcast"
license=('GPL3')
depends=('ffmpeg' 'imagemagick' 'gtk3')

source=($url"/archive/v"$pkgver".tar.gz")
md5sums=('edbc2679ae6eb3a02ec0be537f783694')

package() {
  cd "$pkgname-$pkgver"
  make
  ./install "$pkgdir/"
}
