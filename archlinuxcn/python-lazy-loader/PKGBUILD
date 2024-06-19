# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=lazy-loader
pkgname=python-lazy-loader
pkgver=0.4
pkgrel=3
pkgdesc='Populate library namespace without incurring immediate import costs'
arch=('any')
url='https://github.com/scientific-python/lazy_loader'
license=('BSD-3-Clause')
depends=(
  python
)
makedepends=(
  python-flit-core
  python-build
  python-wheel
  python-installer
  python-setuptools
)
checkdepends=(
  python-pytest
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/scientific-python/lazy_loader/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('3512488bbb3f1699adcbcc7461715d208191b02f8b43b77cc73e703600b13aa7bed62575ffc98ab210ccdb05e8004d5f8f22eaca33fc780afbc1474c15ace8c2')

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
  rm -rfv ${pkgdir}${site_packages}/lazy_loader/tests
}
# vim:set ts=2 sw=2 et:
