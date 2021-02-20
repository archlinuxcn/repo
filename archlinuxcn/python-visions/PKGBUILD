# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-visions
_pkgname=visions
pkgver=0.7.1
pkgrel=3
pkgdesc='Type System for Data Analysis in Python'
arch=('any')
url='https://github.com/dylan-profiler/visions'
license=('BSD')
depends=(
  python-attrs
  python-multimethod
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
sha512sums=('788a31e5812fe2a729c1d2d1b3dc5b9816dad970b82084109ca2e1f0d7b0c5b77f29364358d608808a929840690a34f139ad9a0770a2be3e526048e3d3b6911d')

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
