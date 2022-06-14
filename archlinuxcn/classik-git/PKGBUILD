# Maintainer: Rocket Aaron <i at rocka dot me>
# Contributor: Art Dev <artdevjs at gmail dot com>

_pkgname=classik
pkgname=${_pkgname}-git
pkgver=3.0.breeze5.23.80.r60.g880bf320
pkgrel=1
pkgdesc='ClassiK is a highly customizable binary Window Decoration and Application Style plugin for recent versions of the KDE Plasma desktop. It provides the Classik, Kite, Oxygen/Breeze, and Redmond icon styles.'
arch=(x86_64)
url="https://github.com/paulmcauley/classik"
license=(GPL)
replaces=()
depends=(frameworkintegration kdecoration breeze-icons kwayland kirigami2 hicolor-icon-theme)
makedepends=(git extra-cmake-modules kcmutils)
optdepends=('kcmutils: for classik-settings')
provides=()
conflicts=()
source=("${_pkgname}::git+https://github.com/paulmcauley/classik.git#branch=master")
sha256sums=('SKIP')

pkgver () {
  cd "${_pkgname}"
  git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

prepare() {
  cd "${_pkgname}"
  # patch -Np1 -i ...
}

build() {
  cd "${_pkgname}"
  cmake -B build \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_BUILD_TYPE=Release \
    -DBUILD_TESTING=OFF \
    -DKDE_INSTALL_USE_QT_SYS_PATHS=ON
  cmake --build build
}

package() {
  cd "${_pkgname}"
  DESTDIR="${pkgdir}" cmake --install build
}

