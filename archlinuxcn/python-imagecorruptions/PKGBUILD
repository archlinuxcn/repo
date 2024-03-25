# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-imagecorruptions
_pkgname=imagecorruptions
pkgver=1.1.2
pkgrel=4
pkgdesc='Python package to corrupt arbitrary images'
arch=(any)
url='https://github.com/bethgelab/imagecorruptions'
license=('Apache-2.0')
depends=(
  python-numpy
  python-opencv
  python-pillow
  python-scikit-image
  python-scipy
)
makedepends=(
  python-build
  python-installer
  python-setuptools
  python-wheel
)

source=("${pkgname}-${pkgver}.tar.gz::https://github.com/bethgelab/imagecorruptions/archive/v${pkgver}.tar.gz")
sha512sums=('8f903ae552007d8019e37677de49d3903e5e868fc400c4cdb07d9e20891343d139acda2da36e47138d55bb541aeef1e466dc110365feda1e2d0b3ccaa92c6172')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
}
# vim:set ts=2 sw=2 et:
