# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=timeloop
pkgname=python-timeloop
pkgver=1.0.2
pkgrel=7
pkgdesc='An elegant periodic task executor'
arch=('any')
url='https://github.com/sankalpjonn/timeloop'
license=('MIT')
depends=(
  python
)
makedepends=(
  python-build
  python-installer
  python-setuptools
  python-wheel
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/sankalpjonn/timeloop/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('93f40bc82999356e4a32b821c43e2ba3fe9c7bd4b2cb093d7c21f7b60a5bea18f3c9c0f72abfa54ec81d35ff7978a801ac8bcf77c0978c6077de00e2bc96382e')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
