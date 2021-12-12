# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=pydicom-seg
pkgname=python-pydicom-seg
pkgver=0.2.3
pkgrel=1
pkgdesc='Python package for DICOM-SEG medical segmentation file reading and writing'
arch=('x86_64')
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
sha512sums=('a814370c36735003422372eeaa04238394ae525f7382203abd341868a63abd5040bd8aed830191cdc7a9b1c695278f9f0c2275fe93061398e157af565aae65f0')

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
