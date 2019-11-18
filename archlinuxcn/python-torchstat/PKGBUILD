# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-torchstat
_pkgname=torchstat
pkgver=0.0.7
pkgrel=2
pkgdesc='Model analyzer in PyTorch'
arch=('any')
url='https://github.com/Swall0w/torchstat'
license=('MIT')
depends=(
  'python-numpy'
  'python-pandas'
  'python-pytorch'
)
makedepends=(
  'python-setuptools'
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/Swall0w/torchstat/archive/${pkgver}.tar.gz")
sha512sums=('eb5f25fcf211114a67ec7a6f87c941f02b7d8a051d05e0e7d7c085017ec98eecf7afb8136c60a7fc7c8396e65c68e06ecc2cc0936239fb3cade71a3df42ddcb5')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
