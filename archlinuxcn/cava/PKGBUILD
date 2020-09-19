# Maintainer: Nissar Chababy <funilrys at outlook dot com>
# Ex-Maintainer: Celestial Walrus <aur@celestial.cf>

pkgname=cava
pkgver=0.7.2
pkgrel=2
pkgdesc='Console-based Audio Visualizer for Alsa'
arch=('any')
url='https://github.com/karlstav/cava'
license=('MIT')
depends=('fftw' 'alsa-lib' 'ncurses' 'iniparser' 'portaudio')
optdepends=('sndio' 'pulseaudio')
makedepends=('autoconf' 'automake')
source=("https://github.com/karlstav/cava/archive/${pkgver}.tar.gz")
sha512sums=('f1bc3af88fa167bdd966331f34ac7bd87063c5f2ba0bc440665a2fbadb0b8d1004775ce2511709d2e3c9d1c854d3acffe1c0fa6d951a8005d9dd56c0636568a5')

build() {
  cd ${pkgname}-${pkgver}
  ./autogen.sh
  ./configure --prefix=/usr
  make
}

package() {
  cd ${pkgname}-${pkgver}
  install -Dm755 cava "$pkgdir/usr/bin/cava"
  install -Dm644 LICENSE "$pkgdir"/usr/share/licenses/"${pkgname}"/LICENSE
}
