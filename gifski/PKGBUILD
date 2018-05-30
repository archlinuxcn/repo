# Maintainer: Philipp Wolfer <ph.wolfer@gmail.com>
pkgname=gifski
pkgver=0.8.2
pkgrel=2
pkgdesc="GIF encoder based on libimagequant (pngquant, gifquant?). Squeezes maximum possible quality from the awful GIF format"
arch=('i686' 'x86_64')
url="https://gif.ski/"
license=('AGPL3')
depends=(gcc-libs)
makedepends=(rust clang)
source=(
  ${pkgname}-${pkgver}.tar.gz::https://github.com/ImageOptim/${pkgname}/archive/${pkgver}.tar.gz
  dynamic-openmp.patch
)
sha256sums=(
  'd7bf1b6515c273b822c94fc78e6d10fbc45d444a04bc3487fe3e799d6aa836e0'
  'be6480ba294bab01ae8651ca3b4c8cbcbe28f6bc920cc6afc2e9dd6c2c62d14f'
)

prepare() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  patch -p1 -i ${srcdir}/dynamic-openmp.patch
}

build() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  cargo build --release --features=openmp
}

package() {
  cd "${srcdir}/${pkgname}-${pkgver}"
  install -Dm755 target/release/gifski "$pkgdir/usr/bin/gifski"
}
