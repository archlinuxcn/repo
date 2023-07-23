# Maintainer: Carlos Aznarán <caznaranl@uni.pe>
# Contributor: Michel Zou <xantares09@hotmail.com>
_base=multiprocess
pkgname=python-${_base}
pkgdesc="better multiprocessing and multithreading in python"
pkgver=0.70.15
pkgrel=1
url="https://github.com/uqfoundation/${_base}"
arch=(any)
license=('custom:BSD-3-clause')
depends=(python-dill)
makedepends=(python-setuptools)
source=(${url}/archive/${_base}-${pkgver}.tar.gz)
sha512sums=('b2413ad24c2c8af5b962b22e2343e77e7f33e271f763b3a5426f945d6869bc3684645e62dec80234c10506d12e2bed3edd725a796d75d87409372210032930b8')

build() {
  cd ${_base}-${_base}-${pkgver}
  python setup.py build
}

package() {
  cd ${_base}-${_base}-${pkgver}
  PYTHONPYCACHEPREFIX="${PWD}/.cache/cpython/" python setup.py install --prefix=/usr --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm 644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
