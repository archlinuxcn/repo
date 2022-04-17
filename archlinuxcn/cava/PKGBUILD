# Maintainer: Nissar Chababy <funilrys at outlook dot com>
# Ex-Maintainer: Celestial Walrus <aur@celestial.cf>

pkgname=cava
pkgver=0.8.1
pkgrel=2
pkgdesc='Console-based Audio Visualizer for Alsa'
arch=('any')
url='https://github.com/karlstav/cava'
license=('MIT')
makedepends=('vim')
depends=('fftw' 'alsa-lib' 'ncurses' 'iniparser')
optdepends=('sndio' 'pulseaudio' 'portaudio')
source=("$pkgname-$pkgver.tar.gz::https://github.com/karlstav/cava/archive/${pkgver}.tar.gz")
sha512sums=('fad4e4fefe98300cc2774a168322056e4181cd2a0cc77a8622471d86512bab9eea6c09559a75518785fbcafee5a958e6d95c8fe5ce1816253e4dec99a23fae1c')

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
