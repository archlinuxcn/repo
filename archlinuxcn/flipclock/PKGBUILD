# Maintainer: Alynx Zhou <alynx.zhou@gmail.com>
pkgname=flipclock
pkgver=2.4.0
pkgrel=1
pkgdesc="A flip clock screensaver supported by SDL2."
arch=('x86_64' 'i686' 'aarch64' 'armv7h' 'armv6h')
url="https://github.com/AlynxZhou/flipclock"
license=('Apache')
depends=('sdl2' 'sdl2_ttf')
makedepends=('cmake')
source=("https://github.com/AlynxZhou/${pkgname}/archive/v${pkgver}.tar.gz")
sha512sums=('dfd0e18bcb34532a1db0f1b56eac6926a06c5d95b95b04501e7ae410742dd2177d9abc5dba3b0aa404475e373d511efe7acf6d8efd0ee49bc911d5e927e082ee')

prepare() {
  mkdir -p build
}

build() {
  cd build
  cmake -DCMAKE_INSTALL_PREFIX=/usr "../${pkgname}-${pkgver}"
  make
}

package() {
  cd build
  make DESTDIR="${pkgdir}/" install
}

