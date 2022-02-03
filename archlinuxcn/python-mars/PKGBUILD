# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=mars
pkgname=python-mars
pkgver=0.8.1
pkgrel=1
pkgdesc='A tensor-based unified framework for large-scale data computation which scales Numpy, pandas, Scikit-learn and Python functions'
arch=('x86_64')
url='https://github.com/mars-project/mars'
license=(Apache)
depends=(
  python-arrow
  python-cloudpickle
  python-gevent
  python-jinja
  python-lz4
  python-numexpr
  python-numpy
  python-pandas
  python-protobuf
  python-psutil
  python-requests
  python-scikit-learn
  python-scipy
  python-sqlalchemy
)
makedepends=(
  cython
  python-setuptools
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/mars-project/mars/archive/v${pkgver}.tar.gz")
sha512sums=('50054ce7e9861e293e640a56a16ef51cb8fe47fe9a807e0b2b4b8c70fdef4d0cee69257bae18b110da6ac657908be16262593158f57e7cceed10f2a07ac28c05')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
# vim:set ts=2 sw=2 et:
