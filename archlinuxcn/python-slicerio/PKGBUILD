# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=slicerio
pkgname=python-slicerio
pkgver=0.1.5
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
sha512sums=('b7d6a96b7d434c8b411fc049793691585f2047b533113b12ac7a5ea6a10fadbac2cf97cb5d135742e28116818c831e4f176dd7954cf497f5ce37592d43d0d348'
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
