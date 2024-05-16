# Maintainer: Nissar Chababy <funilrys at outlook dot com>
# Ex-Maintainer: Celestial Walrus <aur@celestial.cf>

pkgname=cava
pkgver=0.10.2
pkgrel=2
pkgdesc='Console-based Audio Visualizer for Alsa'
arch=('any')
url='https://github.com/karlstav/cava'
license=('MIT')
depends=('fftw' 'alsa-lib' 'ncurses' 'iniparser' 'sndio' 'portaudio')
optdepends=('pulseaudio' 'pipewire')
makedepends=('sndio' 'portaudio' 'libpulse' 'm4' 'automake' 'autoconf' 'libpipewire')
source=("$pkgname-$pkgver.tar.gz::https://github.com/karlstav/cava/archive/${pkgver}.tar.gz")
sha512sums=('c28ef5a89668b8f90a3b4cbf71b208dd067268d5ed9eca35ff3881bfab0fd7bf72efe2164f29af47ca7972637d8f1d6a86ff2b2e0c9c9221a1856d8dfa960065')

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
