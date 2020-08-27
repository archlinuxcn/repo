# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-lvis-openmm-git
_pkgname=lvis
_pkgver=10.5.2
pkgver=10.5.2.r215.9fa16b4
pkgrel=1
pkgdesc='Python API for LVIS Dataset (openmm lab fork)'
arch=('any')
url='https://github.com/open-mmlab/cocoapi'
license=(BSD)
depends=(
  opencv
  python-cycler
  python-dateutil
  python-kiwisolver
  python-matplotlib
  python-numpy
  python-pyparsing
  python-pycocotools-openmm
  python-six
)
makedepends=(
  git
  python-pip
  python-setuptools
)
provides=(python-lvis python-lvis-openmm)
conflicts=(python-lvis python-lvis-openmm)

source=("${_pkgname}::git+https://github.com/open-mmlab/cocoapi.git")
sha512sums=('SKIP')

pkgver() {
  cd "${_pkgname}"
  printf "%s.r%s.%s" "${_pkgver}" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build() {
  cd "${_pkgname}/${_pkgname}"
  python setup.py build
}

package() {
  cd "${_pkgname}/${_pkgname}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 "${srcdir}/${_pkgname}/license.txt" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
