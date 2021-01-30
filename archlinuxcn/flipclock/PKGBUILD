# Maintainer: Alynx Zhou <alynx.zhou@gmail.com>
pkgname=flipclock
pkgver=2.7.0
pkgrel=1
pkgdesc="A flip clock screensaver supported by SDL2."
arch=('x86_64' 'i686' 'aarch64' 'armv7h' 'armv6h')
url="https://github.com/AlynxZhou/flipclock"
license=('Apache')
depends=('sdl2' 'sdl2_ttf')
makedepends=('meson')
source=("https://github.com/AlynxZhou/${pkgname}/archive/v${pkgver}.tar.gz")
sha512sums=('691fa8a4905156a872f3be003f2ff5f0b4fd17ec1b2adb7a33ec24435265c9ddcd961c8bfbf8f4d2ddd11ef3148ac3ecb0e8029cb428286270346c8deb896a32')

prepare() {
  mkdir -p build
}

build() {
  cd build
  arch-meson . "../${pkgname}-${pkgver}"
  meson compile
}

package() {
  cd build
  DESTDIR="${pkgdir}" meson install
}
