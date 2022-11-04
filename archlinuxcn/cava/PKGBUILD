# Maintainer: Nissar Chababy <funilrys at outlook dot com>
# Ex-Maintainer: Celestial Walrus <aur@celestial.cf>

pkgname=cava
pkgver=0.8.3
pkgrel=1
pkgdesc='Console-based Audio Visualizer for Alsa'
arch=('any')
url='https://github.com/karlstav/cava'
license=('MIT')
depends=('fftw' 'alsa-lib' 'ncurses' 'iniparser' 'sndio' 'portaudio')
optdepends=('pulseaudio')
makedepends=('sndio' 'portaudio' 'libpulse')
source=("$pkgname-$pkgver.tar.gz::https://github.com/karlstav/cava/archive/${pkgver}.tar.gz")
sha512sums=('cd176428ff293572325d21769fd4fdb666b6301e0fe5c7a2c53af2399a26b3fd10e83647f9c9cc318f4c69cc28835323fb949cd76340c14670df8b544bffa0f0')

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
