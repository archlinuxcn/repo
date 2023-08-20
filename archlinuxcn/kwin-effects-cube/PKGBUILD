# Maintainer: Vlad Zahorodnii <contact@vladzahorodnii.com>

pkgname=kwin-effects-cube
pkgver=2.0.0
pkgrel=2
pkgdesc='Desktop cube effect for KWin'
arch=('x86_64')
url='https://github.com/zzag/kwin-effects-cube'
license=('GPL3')
depends=('kwin>=5.25.0' qt5-quick3d)
makedepends=(extra-cmake-modules)
conflicts=('kwin-effects-cube-git')
source=("${pkgname}-${pkgver}.zip::https://github.com/zzag/kwin-effects-cube/archive/refs/tags/${pkgver}.zip")
sha256sums=('bb83c04815faf3ce2c62c5f643ba9e38368eeb7694917a61fec9e83cc5de66f4')

build() {
    cmake -B build -S "${pkgname}-${pkgver}" \
        -DCMAKE_INSTALL_PREFIX=/usr \
        -DCMAKE_INSTALL_LIBDIR=lib
    cmake --build build
}

package() {
    DESTDIR="${pkgdir}" cmake --build build --target install
}
