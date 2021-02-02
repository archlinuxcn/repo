# Maintainer: Alynx Zhou <alynx.zhou@gmail.com>
pkgname=flipclock
pkgver=2.8.0
pkgrel=1
pkgdesc="A flip clock screensaver supported by SDL2."
arch=('x86_64' 'i686' 'aarch64' 'armv7h' 'armv6h')
url="https://github.com/AlynxZhou/flipclock"
license=('Apache')
depends=('sdl2' 'sdl2_ttf')
makedepends=('meson')
source=("https://github.com/AlynxZhou/${pkgname}/archive/v${pkgver}.tar.gz")
sha512sums=('9acdc9a99fbc70841c02faa6f9af6e9314415e09ffb43746fba7da1c3963794b39c3e329b2175d838a421c72074a390a751358840c4e27d3bc7bb4c7ec347907')

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
