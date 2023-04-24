# Maintainer: Integral <integral@murena.io>

pkgname=futuresql-git
_pkgname=futuresql
pkgver=0.1.0_r52.g4d24ce2
pkgrel=1
pkgdesc="Non-blocking Qt database framework"
arch=('x86_64')
url="https://invent.kde.org/libraries/futuresql"
license=(BSD LGPL)
depends=('qcoro-qt5')
makedepends=('git' 'extra-cmake-modules')
provides=('futuresql')
conflicts=('futuresql')
source=("git+${url}.git")
sha256sums=('SKIP')

pkgver() {
  cd "${_pkgname}"
  _ver="$(grep -m1 'project(futuresql LANGUAGES CXX VERSION' CMakeLists.txt | cut -d '"' -f2)"
  echo "${_ver}_r$(git rev-list --count HEAD).g$(git rev-parse --short HEAD)"
}

build() {
  cd "${_pkgname}"
  cmake -DCMAKE_INSTALL_PREFIX=/usr -B build
  make -C build
}

package() {
  cd "${_pkgname}"
  make -C build DESTDIR="${pkgdir}" PREFIX=/usr install

  install -Dm644 LICENSES/* -t ${pkgdir}/usr/share/licenses/${pkgname}/
}
