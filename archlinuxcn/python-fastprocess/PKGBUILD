# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-fastprocess
_pkgname=fastprocess
pkgver=2.1.0
pkgrel=1
pkgdesc='A fast subprocess library'
arch=('any')
url='https://github.com/dstathis/fastprocess'
license=('LGPL-3.0-or-later')
depends=(
  python
)
makedepends=(
  python-build
  python-hatchling
  python-installer
  python-setuptools
  python-wheel
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/dstathis/fastprocess/archive/${pkgver}.tar.gz")
sha512sums=('63f62f3dbb3311ef6ee555fcd5686f6ec3b304c1719d680c83cc72045ba20c8bb72f31eac381a6a5f7b6f8c8bd18bed2979e914d0b09d9cb870300a31d513fc9')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
# vim:set ts=2 sw=2 et:
