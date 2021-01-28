# Maintainer: Alynx Zhou <alynx.zhou@gmail.com>
pkgname=flipclock
pkgver=2.5.0
pkgrel=1
pkgdesc="A flip clock screensaver supported by SDL2."
arch=('x86_64' 'i686' 'aarch64' 'armv7h' 'armv6h')
url="https://github.com/AlynxZhou/flipclock"
license=('Apache')
depends=('sdl2' 'sdl2_ttf')
makedepends=('meson')
source=("https://github.com/AlynxZhou/${pkgname}/archive/v${pkgver}.tar.gz")
sha512sums=('559d4a7552d4f7cc960592d832347b6b4a6d243577198b5da11eab1fef0cb1276b342ba2ae4c1f4be1b35821fccbd526c0fd2469c068dd204438458a15b87677')

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
  DESTDIR="${pkgdir}/" meson install
}
