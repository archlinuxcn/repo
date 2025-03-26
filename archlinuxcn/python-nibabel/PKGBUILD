# Maintainer: Butui Hu <hot123tea123@gmail.com>
# Contributor: Thomas Roos <mail [at] thomasroos.nl>
# Contributor: Liam Timms <timms5000@gmail.com>
# Contributor: wedjat <wedjat@protonmail.com>
# Contributor: Masoud <mpoloton@gmail.com>

pkgname=python-nibabel
_pkgname=nibabel
pkgver=5.3.2
pkgrel=3
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
sha512sums=('b06db6273947d1024380049b3353eabf086271ce7990dad937aac39057795cdf294bab5bc6b4fb2b23406278ff0287c8cfc10ea77d209c4292f34acbba08cd3e')

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
