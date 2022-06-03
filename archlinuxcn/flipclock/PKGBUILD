# Maintainer: Alynx Zhou <alynx.zhou@gmail.com>
pkgname=flipclock
pkgver=2.9.2
pkgrel=1
pkgdesc="A flip clock screensaver supported by SDL2."
arch=('x86_64' 'i686' 'aarch64' 'armv7h' 'armv6h')
url="https://github.com/AlynxZhou/flipclock"
license=('Apache')
depends=('sdl2' 'sdl2_ttf')
makedepends=('meson')
source=("https://github.com/AlynxZhou/${pkgname}/archive/v${pkgver}.tar.gz")
sha512sums=('96db65b21307cd93f3495d5504978fa6d0dfcbf5a4f6ba12d91e74d5753e32d3dd20c6d49bdcd6c838805f97871a56ce3818db195f0599135e1b8292567fdbf8')

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
