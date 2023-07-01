# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=lazy_loader
pkgname=python-lazy-loader
pkgver=0.3
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
sha512sums=('559fc96a032ba3882e0e7fe5c85dadf1694b42858cb08ac1d51c7bf972d40ff98aa5c4b07fc855b79369c6e046f717ff141a4bd0554aec8318185f8f20be2a70')

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
