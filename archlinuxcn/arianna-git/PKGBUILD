# Maintainer: Integral <integral@murena.io>

pkgname=arianna-git
_pkgname=arianna
pkgver=1.0.0_r241.g0a4b523
pkgrel=1
pkgdesc="EPub Reader for mobile devices"
groups=('kde-applications-git')
url="https://invent.kde.org/graphics/${_pkgname}.git"
depends=('kirigami-addons' 'hicolor-icon-theme')
arch=('x86_64')
license=('GPL' 'LGPL' 'MIT' 'BSD')
makedepends=('git' 'extra-cmake-modules' 'kdoctools' 'kfilemetadata' 'qqc2-desktop-style' 'python' 'reuse' 'baloo' 'qt5-websockets' 'qt5-webengine')
provides=('arianna')
conflicts=('arianna')
source=(git+https://invent.kde.org/graphics/${_pkgname}.git)
sha256sums=('SKIP')

pkgver() {
  cd ${_pkgname}/
  _ver="$(grep -m1 'set *(PROJECT_VERSION' CMakeLists.txt | cut -d '"' -f2)"
  echo "${_ver}_r$(git rev-list --count HEAD).g$(git rev-parse --short HEAD)"
}

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
