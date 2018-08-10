# Maintainer: Philipp Wolfer <ph.wolfer@gmail.com>
pkgname=gifski
pkgver=0.8.4
pkgrel=1
pkgdesc="GIF encoder based on libimagequant (pngquant, gifquant?). Squeezes maximum possible quality from the awful GIF format"
arch=('i686' 'x86_64')
url="https://gif.ski/"
license=('AGPL3')
depends=(gcc-libs)
makedepends=(rust clang)
source=(${pkgname}-${pkgver}.tar.gz::https://github.com/ImageOptim/${pkgname}/archive/${pkgver}.tar.gz)
sha256sums=('e78da4306f01bf4070d7904066f5253058866a9888ca59fc3a08a2a547607b5c')

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  cargo build --release --features=openmp
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  install -Dm755 target/release/gifski "$pkgdir/usr/bin/gifski"
}
