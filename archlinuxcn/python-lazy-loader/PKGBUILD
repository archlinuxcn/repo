# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=lazy_loader
pkgname=python-lazy-loader
pkgver=0.1
pkgrel=1
pkgdesc='Populate library namespace without incurring immediate import costs'
arch=('any')
url='https://github.com/scientific-python/lazy_loader'
license=('BSD')
depends=(
  python
)
makedepends=(
  python-flit-core
  python-build
  python-wheel
  python-installer
)
checkdepends=(
  python-pytest
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/scientific-python/lazy_loader/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('d3469d7d07ebb3459d599b8346f4fd91ab8ea98c6c5a62c2f3159a7beebbb7e7c8b033b9c442d93de923d847a7f3f5bf2c5db3419da961589cee8bed5c6ab0f3')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

check() {
  cd "${_pkgname}-${pkgver}"
  pytest -v
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm644 LICENSE.md -t "${pkgdir}/usr/share/licenses/${pkgname}"

  local site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  rm -rfv ${pkgdir}${site_packages}/${_pkgname}/tests
}
# vim:set ts=2 sw=2 et:
