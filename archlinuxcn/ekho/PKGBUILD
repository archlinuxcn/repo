# Maintainer: guoyizhang <myname at malacology dot net>
# Contributor: 0b100100 <0b100100 at protonmail dot ch>
# Contributor: Denis Kasak <dkasak|AT|termina.org.uk>

pkgname=ekho
pkgver=8.9.3
pkgrel=1
pkgdesc="Multilingual text-to-speech (TTS) software for Cantonese, Mandarin, Toisanese, Zhaoan Hakka, Tibetan, Ngangien, Korean and English"
arch=('i686' 'x86_64')
url="https://www.eguidedog.net/ekho.php"
license=('GPL')
depends=('espeak-ng' 'lame')
makedepends=('git' 'autoconf' 'make' 'utf8cpp')
source=("git+https://github.com/hgneng/ekho.git#tag=v${pkgver}")
sha512sums=('SKIP')

build() {
  cd "$pkgname"
  autoreconf --install
  CXXFLAGS="$CXXFLAGS -I/usr/include/utf8cpp/" \
  ./configure --prefix=/usr --with-mp3lame
  make
}

package() {
  cd "$pkgname"
  make DESTDIR="$pkgdir/" install
}
