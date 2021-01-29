# Maintainer: Alynx Zhou <alynx.zhou@gmail.com>
pkgname=flipclock
pkgver=2.6.2
pkgrel=1
pkgdesc="A flip clock screensaver supported by SDL2."
arch=('x86_64' 'i686' 'aarch64' 'armv7h' 'armv6h')
url="https://github.com/AlynxZhou/flipclock"
license=('Apache')
depends=('sdl2' 'sdl2_ttf')
makedepends=('meson')
source=("https://github.com/AlynxZhou/${pkgname}/archive/v${pkgver}.tar.gz")
sha512sums=('a591cae78cfb79408211c1820e559a1b0ab8b612a4744d35ce4e7526bc08fbf3da3d8aec04b98809dbeabf0f26937c77e487ce54655e65cb5f57804ecc82ecab')

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
