# Maintainer: Rocket Aaron <i at rocka dot me>
# Contributor: Art Dev <artdevjs at gmail dot com>

pkgname=klassy
pkgver=4.3.breeze5.27.5
pkgrel=1
pkgdesc='Klassy is a highly customizable binary Window Decoration and Application Style plugin for recent versions of the KDE Plasma desktop. It provides the Klassy, Kite, Oxygen/Breeze, and Redmond icon styles.'
arch=(x86_64)
url="https://github.com/paulmcauley/klassy"
license=(GPL)
replaces=(classik)
depends=(frameworkintegration kdecoration breeze-icons kwayland kirigami2 hicolor-icon-theme)
makedepends=(extra-cmake-modules kcmutils)
optdepends=('kcmutils: for klassy-settings')
provides=()
conflicts=()
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('ed73612598fa78b5d47706c54ef15f00722e44296cf79f652ffe5d601ce46a18')

build() {
  cd "${pkgname}-${pkgver}"
  cmake -B build \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_TESTING=OFF \
    -DKDE_INSTALL_USE_QT_SYS_PATHS=ON
  cmake --build build
}

package() {
  cd "${pkgname}-${pkgver}"
  DESTDIR="${pkgdir}" cmake --install build
}

