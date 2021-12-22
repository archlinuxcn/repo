# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=pydicom-seg
pkgname=python-pydicom-seg
pkgver=0.4.0
pkgrel=1
pkgdesc='Python package for DICOM-SEG medical segmentation file reading and writing'
arch=('any')
url='https://github.com/razorx89/pydicom-seg'
license=('MIT')
depends=(
  python-attrs
  python-jsonschema
  python-numpy
  python-pydicom
  python-simpleitk
)
makedepends=(
  python-dephell 
  python-setuptools
)
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/razorx89/pydicom-seg/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('f5aacfe39140d0345d938fec1d42ab5330ffed82e568df440e91e8197666d563bd008ab89c3d96bc5353bb022252f2edcd993105d84c50e94d2c439cbd7133d9')

prepare() {
  cd "${_pkgname}-${pkgver}"
  dephell deps convert --from pyproject.toml --to setup.py
}

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
