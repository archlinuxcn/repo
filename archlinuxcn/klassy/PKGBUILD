# Maintainer: Rocket Aaron <i at rocka dot me>
# Contributor: Art Dev <artdevjs at gmail dot com>

pkgname=klassy
pkgver=5.1.breeze5.27.11
pkgrel=1
pkgdesc='Highly customizable binary Window Decoration, Application Style and Global Theme plugin for recent versions of the KDE Plasma desktop.'
arch=(x86_64)
url="https://github.com/paulmcauley/klassy"
license=('GPL-2.0-or-later AND (GPL-2.0-only OR GPL-3.0-only) AND MIT AND BSD-3-Clause')
replaces=(classik)
depends=(frameworkintegration5 kdecoration5 breeze-icons kwayland5 kirigami2 hicolor-icon-theme)
makedepends=(extra-cmake-modules kcmutils5)
optdepends=('kcmutils5: for klassy-settings')
provides=()
conflicts=()
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/refs/tags/${pkgver}.tar.gz")
sha256sums=('cd155037728d64e8b6eb5f2f72b3c220e5e63ecde071014d07fecb50ab90992d')

build() {
  export CMAKE_PREFIX_PATH="/usr/lib/cmake/plasma5"
  cmake -S "${pkgname}-${pkgver}" -B build \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DBUILD_TESTING=OFF
  cmake --build build
}

package() {
  DESTDIR="${pkgdir}" cmake --install build
}

