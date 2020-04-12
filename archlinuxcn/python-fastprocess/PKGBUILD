# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-fastprocess
_pkgname=fastprocess
pkgver=1.0.1
pkgrel=2
pkgdesc='A fast subprocess library'
arch=('any')
url='https://github.com/dstathis/fastprocess'
license=('LGPL')
makedepends=(
  'python-setuptools'
)
source=("https://github.com/dstathis/fastprocess/archive/${pkgver}.tar.gz")
sha512sums=('4378a2019bfe5d4c5580f4c4ba3fbd98d2c573c97cdd22fbd7e86ec353cfc18e6f93851b3a5c34b79a33ebfe03ec1005f95bedd79cf9524cf5c41645021426d8')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
# vim:set ts=2 sw=2 et:
