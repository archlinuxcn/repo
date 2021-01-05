# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-visions
_pkgname=visions
pkgver=0.7.0
pkgrel=1
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
  python-multimethod
  python-pillow
  python-pydot
  python-pytest
  python-pytest-black
  python-pytest-mypy
  python-shapely
  twine
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/dylan-profiler/visions/archive/v${pkgver}.tar.gz")
sha512sums=('a10a296f2757364b9d1c96043f695f9a1280b23284aee515aec2c66cd3472b491467f33160170b39344c2bf519fa3ede0cc060ade318dc01eb4f93e6219901a1')

build() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python setup.py build
}

check() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  PYTHONPATH="${PWD}/build/lib" pytest -v
}

package() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
