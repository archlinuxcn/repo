# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=gluon-cv
pkgname=python-gluoncv
pkgver=0.5.0
pkgrel=2
pkgdesc='A Deep Learning Toolkit for Computer Vision'
arch=(any)
url='https://gluon-cv.mxnet.io'
license=('Apache')
depends=(
  'mxnet'
  'python-matplotlib'
  'python-numpy'
  'python-scipy'
)
makedepends=(python-setuptools)
source=("${pkgname}-${pkgver}.tar.gz"::"https://github.com/dmlc/gluon-cv/archive/v${pkgver}.tar.gz")
sha512sums=('b50f7ca9232cf8657c2953a7501f197225b389a767f9a0a7f4453a239700a198077472c8a21924bba6a1f32909b708becb00841bff5326cb6b42e94f9c23ca4d')

build() {
  cd ${_pkgname}-${pkgver}
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  # install missing json files
  find "${srcdir}/${_pkgname}-${pkgver}/gluoncv/model_zoo/pruned_resnet" -type f -name "*.json" -exec install -Dm644 {} -t "${pkgdir}/usr/lib/python3.7/site-packages/gluoncv/model_zoo/pruned_resnet" \;
  find "${srcdir}/${_pkgname}-${pkgver}/gluoncv/model_zoo/quantized" -type f -name "*.json" -exec install -Dm644 {} "${pkgdir}/usr/lib/python3.7/site-packages/gluoncv/model_zoo/quantized" \;
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
