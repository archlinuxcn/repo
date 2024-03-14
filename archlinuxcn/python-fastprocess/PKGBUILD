# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-fastprocess
_pkgname=fastprocess
pkgver=2.0.0
pkgrel=5
pkgdesc='A fast subprocess library'
arch=('any')
url='https://github.com/dstathis/fastprocess'
license=('LGPL-3.0-or-later')
makedepends=(
  python-build
  python-installer
  python-setuptools
  python-wheel
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/dstathis/fastprocess/archive/${pkgver}.tar.gz")
sha512sums=('194bcf0b1ee094a836df624514b8125712431ef57f01063e6cf799dd3cae3e45b1573756cd8c8eec03837632159a5cd99e0d0cbab864d0dea0ab9527eb4d6a1f')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
# vim:set ts=2 sw=2 et:
