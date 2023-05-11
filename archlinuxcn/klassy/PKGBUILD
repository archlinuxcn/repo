# Maintainer: Rocket Aaron <i at rocka dot me>
# Contributor: Art Dev <artdevjs at gmail dot com>

pkgname=klassy
pkgver=4.2.breeze5.26
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
sha256sums=('d775adca67be5eaf060b20ac022050507963d899e1b294c366415ec1dc53383a')

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

