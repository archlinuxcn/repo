# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=mmsegmentation
pkgname=python-mmsegmentation
pkgver=0.30.0
pkgrel=1
epoch=1
pkgdesc='OpenMMLab Semantic Segmentation Toolbox and Benchmark'
arch=('any')
url='https://github.com/open-mmlab/mmsegmentation'
license=('Apache')
depends=(
  python-matplotlib
  python-mmclassification
  python-mmcv
  python-numpy
  python-prettytable
)
makedepends=(
  python-setuptools
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/open-mmlab/mmsegmentation/archive/v${pkgver}.tar.gz")
sha512sums=('41e83eab33bd48efb05fdc98c9fb7e49106d40ba015ffa3be67a778ec8a67867f462b83157a43b40a69039e0a57939c72b9a4085b64592646d86258f43628ea4')

build() {
  cd "${srcdir}/${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  local site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  # remove unneeded files
  rm -rf "${pkgdir}${site_packages}/tests"
}
# vim:set ts=2 sw=2 et:
