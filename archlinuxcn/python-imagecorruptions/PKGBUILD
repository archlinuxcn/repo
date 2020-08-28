# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-imagecorruptions
_pkgname=imagecorruptions
pkgver=1.1
pkgrel=2
pkgdesc='Python package to corrupt arbitrary images'
arch=(any)
url='https://github.com/bethgelab/imagecorruptions'
license=('Apache')
depends=(
  opencv
  python-numpy
  python-pillow
  python-scikit-image
  python-scipy
)
makedepends=(
  python-setuptools
)

source=("${pkgname}-${pkgver}.tar.gz::https://github.com/bethgelab/imagecorruptions/archive/v${pkgver}.tar.gz")
sha512sums=('4492a2c48ad9c7b6d232f5aae8bca5268bde9ac94b35dfb0cc16ca9cf5a976865fa4d818b9d6464cff79b75653b8c34c763022daf0a21d2203aff97740d055d8')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
}
# vim:set ts=2 sw=2 et:
