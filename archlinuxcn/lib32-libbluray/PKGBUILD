# Maintainer: Tod Jackson <tod.jackson@gmail.com>
# Contributor: Michael Armbruster <michael at armbrust dot me>
# Contributor: Johannes Dewender  arch at JonnyJD dot net
# Contributor: josephgbr <rafael.f.f1@gmail.com>

_pkgbase=libbluray
pkgname=lib32-${_pkgbase}
pkgver=1.2.0
pkgrel=1
pkgdesc="Library to access Blu-Ray disks for video playback (32 bit)"
arch=('x86_64')
url="http://www.videolan.org/developers/libbluray.html"
license=('LGPL2.1')
depends=("$_pkgbase" 'lib32-fontconfig' 'lib32-glibc' 'lib32-freetype2' 'lib32-libxml2')
makedepends=('gcc-multilib')
provides=('libbluray.so')
source=("ftp://ftp.videolan.org/pub/videolan/$_pkgbase/$pkgver/$_pkgbase-$pkgver.tar.bz2")
sha512sums=('d10413b6b86ff2d2e7c4b0103546f2142727cc5209ddb7b227aa74e27384f2e0b9abee37bf8ccc5b0cdfcaeebfb0669cf20903a247df278a8ad6dbd27469d324')

build() {
  export CC='gcc -m32'
  export CXX='g++ -m32'
  export PKG_CONFIG_PATH='/usr/lib32/pkgconfig'
  cd $_pkgbase-$pkgver
  
  ./configure --libdir=/usr/lib32 \
    --prefix=/usr \
    --disable-doxygen-doc \
    --disable-bdjava-jar \
    --host=i686-unknown-linux-gnu
  make
}

package() {
  cd $_pkgbase-$pkgver
  make DESTDIR="$pkgdir" install
  rm -rf "${pkgdir}"/usr/{bin,include,share}
}

# vim:set ts=2 sw=2 et:
