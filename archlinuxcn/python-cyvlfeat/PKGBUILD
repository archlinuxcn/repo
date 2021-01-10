# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=cyvlfeat
pkgname=python-cyvlfeat
pkgver=0.7.0
pkgrel=1
pkgdesc='A thin Cython wrapper around select areas of vlfeat'
arch=('x86_64')
url='https://github.com/menpo/cyvlfeat/'
license=('BSD')
depends=(
  python-numpy
  python-scipy
  python-matplotlib
  vlfeat
)
makedepends=(
  cython
  python-setuptools
)
checkdepends=(
  python-pytest
  python-scikit-image
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/menpo/cyvlfeat/archive/v${pkgver}.tar.gz")
sha512sums=('57a71c8f158a0aa3d29957fc8ddc90ebccce88a3855d2c7da86ef40d3c449f2a360615b1140d01fa72877c70ef6161313f9b3278e389c40a7e07b00daa507ec6')

build() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python setup.py build_ext --inplace
  python setup.py build
}

check() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  pytest -v
}

package() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 "LICENSE.txt" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
