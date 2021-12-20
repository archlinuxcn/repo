# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=pydicom-seg
pkgname=python-pydicom-seg
pkgver=0.3.0
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
sha512sums=('d0eaaa08726eb95c42b251ac53b268cf8f9db3ceddcab18742c29b9d7f2cfa5e94726561ea5780af55762fbb91707ca0ae0a083eb0cc969db8193523aab9a80e')

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
