# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=batchgenerators
pkgname=python-batchgenerators
pkgver=0.19.5
pkgrel=2
pkgdesc='A framework for data augmentation for 2D and 3D image classification and segmentation'
arch=('any')
url='https://github.com/MIC-DKFZ/batchgenerators'
license=('Apache')
depends=(
  'python-numpy'
  'python-scikit-image'
  'python-scikit-learn'
  'python-scipy'
  'python-threadpoolctl'
)
makedepends=(
  'python-setuptools'
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/MIC-DKFZ/batchgenerators/archive/v${pkgver}.tar.gz")
sha512sums=('aa70b531b65c417e7ce30521b706c79f1677281f96389876e38800cb2e1a884fef4095d5aec969af3eee731880daee36c5e6b96e6bccd038bcb250996e7035ca')

get_pyver () {
  python -c 'import sys; print(str(sys.version_info[0]) + "." + str(sys.version_info[1]))'
}

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
  # delete test files
  rm -rfv "${pkgdir}/usr/lib/python$(get_pyver)/site-packages/tests"
}
# vim:set ts=2 sw=2 et:
