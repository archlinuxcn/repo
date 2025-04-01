# Maintainer: Cassandra Watergate (saltedcoffii) <cassandrawatergate@outlook.com>

_pkgname=ffmpeg-audio-thumbnailer
pkgname=$_pkgname
pkgver=1.2.0
pkgrel=1
pkgdesc="A minimal audio file thumbnailer for file managers, such as nautilus, dolphin, thunar, and nemo."
url="https://github.com/saltedcoffii/ffmpeg-audio-thumbnailer"
arch=(any)
depends=('ffmpeg')
license=('GPL3 or any later version')
conflicts=('ffmpeg-audio-thumbnailer-git')
conflicts+=('ffmpegthumbnailer-mp3') # The files don't conflict, but the functions do (this package does it better ;) )
source=("$pkgname-$pkgver.tar.gz::$url/archive/$pkgver.tar.gz")
sha512sums=('6207514443372497b6af3a67a70865a5a0f5b1c6e78db944dd4eaaa505112d6ece80764e63f7592586dc7fa1a67a69e6334068c61746b082353d7645c5ffb8c9')

build() {
  cd $_pkgname-$pkgver
  make
}

check() {
  cd $_pkgname-$pkgver
  make check
}

package() {
  cd $_pkgname-$pkgver
  make DESTDIR="$pkgdir" PREFIX="/usr" install
}
