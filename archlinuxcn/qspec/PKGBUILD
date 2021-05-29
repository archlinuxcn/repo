# Maintainer: Hu Butui <hot123tea123@gmail.com>
# Contributor: Jens Staal <staal1978@gmail.com>

_pkgname=QSpec
pkgname=qspec
pkgver=0.2
pkgrel=1
pkgdesc="A GUI testing library for Qt desktop applications"
arch=('x86_64')
url='https://github.com/ugeneunipro/QSpec'
license=('GPL2')
depends=(
  libxtst
  qt5-webkit
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/ugeneunipro/QSpec/archive/refs/tags/v${pkgver}.tar.gz")
sha256sums=('6f5d44c6b7b7db82ece5238d343fab44f36dc2d3d56afae51bd122acb352d7bd')

build() {
  cd "${_pkgname}-${pkgver}"
  qmake
  make
}

package() {
  cd "${_pkgname}-${pkgver}"
  make INSTALL_ROOT="${pkgdir}/usr/lib" install
}
# vim:set ts=2 sw=2 et:

