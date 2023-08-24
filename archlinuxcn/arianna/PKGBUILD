# Maintainer: Integral <integral@murena.io>

pkgname=arianna
pkgver=23.08.0
pkgrel=1
pkgdesc="EPub Reader for mobile devices"
url="https://invent.kde.org/graphics/${pkgname}"
depends=('kirigami-addons' 'kquickcharts' 'hicolor-icon-theme')
arch=('x86_64' 'aarch64')
license=('GPL' 'LGPL' 'MIT' 'BSD')
makedepends=('git' 'extra-cmake-modules' 'kdoctools' 'kfilemetadata' 'qqc2-desktop-style' 'python' 'reuse' 'baloo' 'qt5-websockets' 'qt5-webengine')
provides=('arianna')
conflicts=('arianna')
source=("https://invent.kde.org/graphics/${pkgname}/-/archive/v${pkgver}/${pkgname}-v${pkgver}.tar.gz")
sha256sums=('c1240da81643fa19bed7978249f61d1b82873b74ac0bd6cce61898ab4d35b115')

prepare() {
  mkdir -p ${pkgname}-v${pkgver}/build/
}

build() {
  cd ${pkgname}-v${pkgver}/build/
  cmake -B build/ -S ../${_pkgname} -DBUILD_TESTING=OFF
  cmake --build build/
}

package() {
  cd ${pkgname}-v${pkgver}/build/
  DESTDIR="${pkgdir}" cmake --install build/
}
