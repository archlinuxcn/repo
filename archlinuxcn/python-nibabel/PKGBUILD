# Maintainer: Butui Hu <hot123tea123@gmail.com>
# Contributor: Thomas Roos <mail [at] thomasroos.nl>
# Contributor: Liam Timms <timms5000@gmail.com>
# Contributor: wedjat <wedjat@protonmail.com>
# Contributor: Masoud <mpoloton@gmail.com>

pkgname=python-nibabel
_pkgname=nibabel
pkgver=5.4.0
pkgrel=1
pkgdesc='Package to access a cacophony of neuro-imaging file formats'
arch=('any')
url='http://nipy.org/nibabel'
license=('MIT')
depends=(
  python-numpy
  python-pillow
  python-pydicom
  python-scipy
  python-six
)
makedepends=(
  python-build
  python-hatch-vcs
  python-hatchling
  python-installer
  python-setuptools
  python-wheel
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/nipy/nibabel/archive/refs/tags/${pkgver}.tar.gz")
sha512sums=('9ba9f904edb591ffa73958f2e3287927578840d79b0fdcdd7653f490bfe0964f1a2acd032d46a1304047ca864ce57a11c4e0e8af245d63942bfb2e033cb1f106')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  # delete unused tests directories
  find ${pkgdir} -depth -type d -name tests -exec rm -rfv {} \;
  install -Dm644 COPYING -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
