# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=slicerio
pkgname=python-slicerio
pkgver=1.1.0
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
  python-setuptools
)

source=("${pkgname}-${pkgver}.tar.gz::https://files.pythonhosted.org/packages/source/${_pkgname::1}/${_pkgname}/${_pkgname}-${pkgver}.tar.gz"
        "https://github.com/lassoan/slicerio/raw/main/LICENSE"
)
sha512sums=('acbc1e758a4ae17dc3bd662617f27e0f4a775bc52621f4e2ad3a594860013656097ab1174cc74f8490965cfd21b46385f40befee7425be6de3356d722fdee380'
            '48efe087bec3e6682a5331ebf9131e78982a1f7371c87c4cb53182beeb86b550b80e8b261e1443f3bb961f7d816faa0c357b4241b173b365a7cf9196b01c6dd4')

build() {
  cd "${_pkgname}-${pkgver}"
  python setup.py build
}

package() {
  cd "${_pkgname}-${pkgver}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 "${srcdir}/LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
