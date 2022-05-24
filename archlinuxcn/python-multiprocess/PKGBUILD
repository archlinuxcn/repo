# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Michel Zou <xantares09@hotmail.com>
_base=multiprocess
pkgname=python-${_base}
pkgdesc="better multiprocessing and multithreading in python"
pkgver=0.70.13
pkgrel=1
url="https://github.com/uqfoundation/${_base}"
arch=(any)
license=('custom:BSD-3-clause')
depends=(python-dill)
makedepends=(python-setuptools)
source=(${url}/archive/${_base}-${pkgver}.tar.gz)
sha512sums=('8d9bb74d86a83c98865055e63db2af31b5393b7d41b61d8173cf1f710e21b1862fc407ab8dca1bc0ed1e2aaaecbfe5c527f00aa17aa67cc576fc1d6d1dcc2c32')

build() {
  cd ${_base}-${_base}-${pkgver}
  python setup.py build
}

package() {
  cd ${_base}-${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python setup.py install --prefix=/usr --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
