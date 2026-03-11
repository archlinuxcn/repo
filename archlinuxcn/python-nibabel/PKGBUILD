# Maintainer: Butui Hu <hot123tea123@gmail.com>
# Contributor: Thomas Roos <mail [at] thomasroos.nl>
# Contributor: Liam Timms <timms5000@gmail.com>
# Contributor: wedjat <wedjat@protonmail.com>
# Contributor: Masoud <mpoloton@gmail.com>

pkgname=python-nibabel
_pkgname=nibabel
pkgver=5.4.1
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
sha512sums=('e495362116ffbb83db2867703dbe573e95c1c3c127ba4a6aa5886b913cee1b513537b71baad9a0cdcd2bfdee7c41707530b14802589582263b0563a48e208f70')

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
