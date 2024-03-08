# Maintainer: Rocket Aaron <i at rocka dot me>
# Contributor: Art Dev <artdevjs at gmail dot com>

_pkgname=klassy
pkgbase="${_pkgname}-git"
pkgname=("${_pkgname}-git"
         "${_pkgname}-qt5-git")
pkgver=4.3.breeze5.27.5.r320.g14713a51
pkgrel=2
pkgdesc='Highly customizable binary Window Decoration and Application Style plugin for recent versions of the KDE Plasma desktop.'
arch=(x86_64)
url="https://github.com/paulmcauley/klassy"
license=('GPL-2.0-only AND GPL-3.0-only AND GPL-2.0-or-later AND LGPL-2.1-or-later AND MIT')
replaces=(classik-git)
depends=(breeze-icons
         hicolor-icon-theme
         frameworkintegration
         gcc-libs
         glibc
         kcmutils
         kcolorscheme
         kconfig
         kcoreaddons
         kdecoration
         kguiaddons
         ki18n
         kiconthemes
         kirigami
         kwidgetsaddons
         kwindowsystem
         qt6-base
         qt6-declarative
         qt6-svg
         xdg-utils)
makedepends=(git
             extra-cmake-modules
             kcmutils5
             frameworkintegration5
             kconfigwidgets5
             kiconthemes5
             kirigami2
             kwindowsystem5)
source=("${_pkgname}::git+https://github.com/paulmcauley/klassy.git#branch=plasma6.0")
sha256sums=('SKIP')

pkgver () {
  cd "${_pkgname}"
  git describe --long --tags | sed 's/\([^-]*-g\)/r\1/;s/-/./g'
}

build() {
  cmake -B build -S "${_pkgname}" \
    -DBUILD_TESTING=OFF \
    -DBUILD_QT5=OFF
  cmake --build build

  CMAKE_PREFIX_PATH="/usr/lib/cmake/plasma5" cmake \
    -B build5 -S "${_pkgname}" \
    -DBUILD_TESTING=OFF \
    -DBUILD_QT6=OFF
  cmake --build build5
}

package_klassy-git() {
  provides=("${_pkgname}")
  conflicts=("${_pkgname}")
  DESTDIR="${pkgdir}" cmake --install build
}

package_klassy-qt5-git() {
  provides=("${_pkgname}-qt5")
  conflicts=("${_pkgname}-qt5")
  depends=("${_pkgname}-git"
           breeze-icons
           gcc-libs
           glibc
           frameworkintegration5
           kconfig5
           kconfigwidgets5
           kguiaddons5
           kiconthemes5
           kirigami2
           kwindowsystem5
           qt5-base
           qt5-declarative
           qt5-svg)
  DESTDIR="${pkgdir}" cmake --install build5
  rm -r "${pkgdir}/usr/share/"{color-schemes,kstyle}
}
