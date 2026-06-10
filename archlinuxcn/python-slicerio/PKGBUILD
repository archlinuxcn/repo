# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=slicerio
pkgname=python-slicerio
pkgver=1.2.0
pkgrel=1
pkgdesc='Utilities for reading and writing files created by 3D Slicer'
arch=('any')
url='https://github.com/lassoan/slicerio'
license=('MIT')
depends=(
  python-numpy
  python-pynrrd
)
makedepends=(
  python-build
  python-installer
  python-setuptools
  python-setuptools-scm
  python-wheel
)

source=("${pkgname}-${pkgver}.tar.gz::https://files.pythonhosted.org/packages/source/${_pkgname::1}/${_pkgname}/${_pkgname}-${pkgver}.tar.gz"
        "https://github.com/lassoan/slicerio/raw/main/LICENSE"
)
sha512sums=('79adabd53db5017103144803c676f06996e97e63a241c74ddf440d9fcb0c4d4200fd703b5a353cdd068703bb25640b241eb07fe2f88dff74d03e9f7ea9cb26bf'
            '48efe087bec3e6682a5331ebf9131e78982a1f7371c87c4cb53182beeb86b550b80e8b261e1443f3bb961f7d816faa0c357b4241b173b365a7cf9196b01c6dd4')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm644 "${srcdir}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
