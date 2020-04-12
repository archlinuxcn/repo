# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=batchgenerators
pkgname=python-batchgenerators
pkgver=0.19.7
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
sha512sums=('b9128f1beee7c57a894b52708a97d1356a31544c1eedfdd29ff68ffb3a4fae75bb082f4ac66b763e559b5aefda83f149fc4983e82e21859da0d0810842e2a1fd')

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
