# Maintainer: Alynx Zhou <alynx.zhou@gmail.com>
pkgname=flipclock
pkgver=2.9.0
pkgrel=1
pkgdesc="A flip clock screensaver supported by SDL2."
arch=('x86_64' 'i686' 'aarch64' 'armv7h' 'armv6h')
url="https://github.com/AlynxZhou/flipclock"
license=('Apache')
depends=('sdl2' 'sdl2_ttf')
makedepends=('meson')
source=("https://github.com/AlynxZhou/${pkgname}/archive/v${pkgver}.tar.gz")
sha512sums=('87409109005fe75dac2047a9eeafd4cd092998ba580a2061d01dda59a58650535655bd21a841508b2ec205da8e6cfd054fca08a4efabd54bf6b58530cf9be658')

prepare() {
  cd "${pkgname}-${pkgver}"
  mkdir -p build
}

build() {
  cd "${pkgname}-${pkgver}/build"
  arch-meson . ..
  meson compile
}

package() {
  cd "${pkgname}-${pkgver}/build"
  DESTDIR="${pkgdir}" meson install
}
