# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=batchgenerators
pkgname=python-batchgenerators
pkgver=0.21
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
sha512sums=('399a5a6757aab9f1f927f4c24fdc7639c8786bfaf0e02aa557a48e72b282c54ad05105a1a81f97fe1ac5d592170868a42d47d175cf72a45677ae509876e42990')

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
