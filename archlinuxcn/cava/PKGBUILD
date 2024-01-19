# Maintainer: Nissar Chababy <funilrys at outlook dot com>
# Ex-Maintainer: Celestial Walrus <aur@celestial.cf>

pkgname=cava
pkgver=0.10.0
pkgrel=1
pkgdesc='Console-based Audio Visualizer for Alsa'
arch=('any')
url='https://github.com/karlstav/cava'
license=('MIT')
depends=('fftw' 'alsa-lib' 'ncurses' 'iniparser' 'sndio' 'portaudio')
optdepends=('pulseaudio')
makedepends=('sndio' 'portaudio' 'libpulse' 'm4' 'automake' 'autoconf')
source=("$pkgname-$pkgver.tar.gz::https://github.com/karlstav/cava/archive/${pkgver}.tar.gz")
sha512sums=('8b54ed59ce7965209f0e03be3409f59b0e59e6a684afca3eb2e3c82c369d35224a0a1a09cbcbca09b36fce416a13efafdff7362fe0b4e2f6b494a023de76793e')

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
