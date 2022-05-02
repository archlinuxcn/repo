# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=batchgenerators
pkgname=python-batchgenerators
pkgver=0.24
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
sha512sums=('6b35313f75b12744d7a08157a54375b7549f12c2092f6f28eb9b5d1571327cfc6370ad150e400c6da2c11870d05b9aff9add6f2a3e4d1e499a2f2fe735fcde83')

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
