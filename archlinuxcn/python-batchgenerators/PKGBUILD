# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=batchgenerators
pkgname=python-batchgenerators
pkgver=0.20.0
pkgrel=1
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
sha512sums=('e223a8b9906448462b942dd6761b1be5cc5809234196c911b21e08b9537ab08c7230f6bb2390f78c26a587b0a032c1e355090d36bab5c6a9870e5990fecbba96')

get_pyver() {
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
