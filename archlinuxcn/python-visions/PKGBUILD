# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-visions
_pkgname=visions
pkgver=0.7.4
pkgrel=1
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
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/dylan-profiler/visions/archive/v${pkgver}.tar.gz")
sha512sums=('0ff3233fd59e1099c138f98fd46d94eb042f1d28c436db41fed5c12dad0a5d6f175db3122fafdbc7d76e0d487a152f530aca4d6aaef165c884f3e2b9d6ed1134')

build() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
