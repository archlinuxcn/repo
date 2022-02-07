# Maintainer: Nissar Chababy <funilrys at outlook dot com>
# Ex-Maintainer: Celestial Walrus <aur@celestial.cf>

pkgname=cava
pkgver=0.7.5
pkgrel=1
pkgdesc='Console-based Audio Visualizer for Alsa'
arch=('any')
url='https://github.com/karlstav/cava'
license=('MIT')
depends=('fftw' 'alsa-lib' 'ncurses' 'iniparser')
optdepends=('sndio' 'pulseaudio' 'portaudio')
source=("$pkgname-$pkgver.tar.gz::https://github.com/karlstav/cava/archive/${pkgver}.tar.gz")
sha512sums=('4bee73ce5b618cae6d2f045b643bb67b5c63de24ba19fa626294f9e1605614a60185c7f008f72671947f59c220387c6a4b51835190361b1bba9cb53cb6fe56b1')

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
