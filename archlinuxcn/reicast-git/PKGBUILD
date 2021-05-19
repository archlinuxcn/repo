# Maintainer: carstene1ns <arch carsten-teibes de> - http://git.io/ctPKG
# Contributor: Holzhaus <jan.holthuis@ruhr-uni-bochum.de>

pkgname=reicast-git
pkgver=20.04.r48.g0bd6ea371
pkgrel=1
pkgdesc="A multiplatform Sega Dreamcast emulator (development version)"
arch=('i686' 'x86_64' 'armv7h')
url="http://reicast.com/"
license=('custom')
conflicts=('reicast')
provides=('reicast')
makedepends=('git')
depends=('libgl' 'alsa-lib' 'libpulse')
optdepends=('python: for joystick configuration utility')
source=(reicast::"git+https://github.com/reicast/reicast-emulator.git")
md5sums=('SKIP')

pkgver() {
  cd reicast
  git describe --long | sed 's/^r//;s/\([^-]*-g\)/r\1/;s/-/./g'
}

build () {
  USE_PULSEAUDIO=1 make -C reicast/reicast/linux PREFIX=/usr
}

package () {
  cd reicast
  make -C reicast/linux DESTDIR="$pkgdir/" PREFIX=/usr install
  # licenses
  install -d "$pkgdir"/usr/share/licenses/$pkgname
  install -m644 LICENSE* "$pkgdir"/usr/share/licenses/$pkgname/
}
