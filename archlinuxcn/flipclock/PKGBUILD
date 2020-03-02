# Maintainer: Alynx Zhou <alynx.zhou@gmail.com>
pkgname=flipclock
pkgver=2.3.7
pkgrel=1
pkgdesc="A flip clock screensaver supported by SDL2."
arch=('x86_64' 'i686' 'aarch64' 'armv7h' 'armv6h')
url="https://github.com/AlynxZhou/flipclock"
license=('GPL')
depends=('sdl2' 'sdl2_ttf')
makedepends=('cmake')
source=("https://github.com/AlynxZhou/${pkgname}/archive/v${pkgver}.tar.gz")
sha512sums=('3f74548ea3400273ad28794e2e4c28dab4bbd381db0e9aded5dd23b9d23199eaf34976d1203ed8bc26e829dcc38781d192e2fcd2ca0fa0e56649e1a4b1a4d27b')

build() {
  cd "${pkgname}-${pkgver}"
  mkdir -p build
  cd build
  cmake -DCMAKE_INSTALL_PREFIX=/usr ..
  make
}

package() {
  cd "${pkgname}-${pkgver}"
  cd build
  make DESTDIR="${pkgdir}/" install
}

