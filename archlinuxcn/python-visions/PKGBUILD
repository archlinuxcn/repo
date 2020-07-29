# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-visions
_pkgname=visions
pkgver=0.4.6
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
  python-pillow
  python-pydot
  python-pytest
  python-pytest-black
  python-pytest-mypy
  python-shapely
  twine
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/dylan-profiler/visions/archive/v${pkgver}.tar.gz")
sha512sums=('3a150b8d613421bdbc615ce73f7a6ed85b6b6a03345008632a0e67cad2efa774264f64adfe7cc99aefae41d523e51fbe77dab449f050495dddfbb2123d75c1e5')

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
