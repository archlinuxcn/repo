# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=pydeck
pkgname=python-pydeck
pkgver=0.7.1
pkgrel=4
pkgdesc='Widget for deck.gl maps'
arch=('any')
url='https://pypi.org/project/pydeck'
license=('Apache')
depends=(
  ipython
  python-ipykernel
  python-ipywidgets
  python-jinja
  python-numpy
  python-traitlets
)
makedepends=(
  python-build
  python-installer
  python-setuptools
  python-wheel
)

source=("${_pkgname}-${pkgver}.tar.gz::https://files.pythonhosted.org/packages/source/${_pkgname::1}/${_pkgname}/${_pkgname}-${pkgver}.tar.gz"
)
sha512sums=('7d4d392a11ae26a9efd138eac6286ed08055613b8aba10ea8888d3d862ef21af13d588ceb6058a5cedbff564fed17b9da5c19f7deeacd6030f0c7dd0ac9afaa3')

prepare() {
  # fix version number
  sed -i "s,0.3.0,${pkgver}," "${_pkgname}-${pkgver}/pyproject.toml"
  # quick fix for building
  sed -i "4i [build-system]" "${_pkgname}-${pkgver}/pyproject.toml"
}

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  mv -vf "${pkgdir}/usr/etc" "${pkgdir}"
}
# vim:set ts=2 sw=2 et:
