# Maintainer: carstene1ns <arch carsten-teibes de> - http://git.io/ctPKG
# Contributor: trya <tryagainprod@gmail.com>
# Contributor: Jan Alexander Steffens (heftig) <jan.steffens@gmail.com>
# Contributor: Tom Newsom <Jeepster@gmx.co.uk>

pkgname=lib32-sdl_sound
pkgver=1.0.3
pkgrel=6
pkgdesc="A library to decode several popular sound file formats, such as .WAV and .MP3 (32 bit)"
arch=('x86_64')
url="http://icculus.org/SDL_sound/"
license=('LGPL')
depends=('lib32-sdl' 'lib32-libmikmod' 'libvorbis' 'lib32-flac' 'lib32-speex' 'lib32-smpeg'
         'lib32-libmodplug' 'sdl_sound')
source=("http://icculus.org/SDL_sound/downloads/SDL_sound-$pkgver.tar.gz")
sha256sums=('3999fd0bbb485289a52be14b2f68b571cb84e380cc43387eadf778f64c79e6df')

build() {
  cd SDL_sound-$pkgver

  export CC="gcc -m32"
  export CXX="g++ -m32"
  export PKG_CONFIG_PATH="/usr/lib32/pkgconfig"
  export SDL_CONFIG=/usr/bin/sdl-config-32
  export CPPFLAGS="$CPPFLAGS -I/usr/include/smpeg"
  ./configure --prefix=/usr --libdir=/usr/lib32 --disable-static
  make
}

package() {
  cd SDL_sound-$pkgver
  make DESTDIR="$pkgdir" install
  # remove stuff already present in sdl_sound package
  rm -rf "$pkgdir"/usr/{bin,include}
}
