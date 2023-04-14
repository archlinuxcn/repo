# Maintainer: Integral <integral@murena.io>

pkgname=arianna
pkgver=1.0.0
pkgrel=1
pkgdesc="EPub Reader for mobile devices"
groups=('kde-applications')
url="https://invent.kde.org/graphics/${pkgname}"
depends=('hicolor-icon-theme')
arch=('x86_64')
license=('GPL' 'LGPL' 'MIT' 'BSD')
makedepends=('git' 'extra-cmake-modules' 'kdoctools' 'kirigami-addons' 'kfilemetadata' 'qqc2-desktop-style' 'python' 'reuse' 'baloo' 'qt5-websockets' 'qt5-webengine')
provides=('arianna')
conflicts=('arianna')
source=("https://invent.kde.org/graphics/${pkgname}/-/archive/v${pkgver}/${pkgname}-v${pkgver}.tar.gz")
sha256sums=('e1b4eea1969d1dc90f9c91714c36c4e73ffa46c4b32e8144d85abdc2679632c8')

prepare() {
  mkdir build/
}

build() {
  cd build/
  cmake -B build/ -S ../${_pkgname} -DBUILD_TESTING=OFF
  cmake --build build/
}

package() {
  cd build/
  DESTDIR="${pkgdir}" cmake --install build/
}
