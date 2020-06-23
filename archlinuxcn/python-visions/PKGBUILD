# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-visions
_pkgname=visions
pkgver=0.4.4
pkgrel=2
pkgdesc='Type System for Data Analysis in Python'
arch=('any')
url='https://github.com/dylan-profiler/visions'
license=('BSD')
depends=(
  python-attrs
  python-networkx
  python-numpy
  python-pandas
  python-tangled-up-in-unicode
)
makedepends=(
  mypy
  python-black
  python-isort
  python-recommonmark
  python-setuptools
  python-sphinx-autodoc-typehints
  python-sphinx_rtd_theme
)
checkdepends=(
  python-imagehash
  python-matplotlib
  python-pillow
  python-pydot
  python-pytest
  python-pytest-black
  python-pytest-mypy
  python-shapely
  twine
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/dylan-profiler/visions/archive/v${pkgver}.tar.gz")
sha512sums=('b9bec32786a5bf9d7c4e26bd6d13f03bf1bee227d697b8416f659f9b7b15f2f346b046d3b65a56988564658d187e0add9cef08368bf303400397b8aa5914a299')

build() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python setup.py build
}

check() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  pytest -v
}

package() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
