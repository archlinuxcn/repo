# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-lvis-git
_pkgname=lvis
_pkgver=0.5.3
pkgver=0.5.3.r19.35f09cd
pkgrel=2
pkgdesc='Python API for LVIS Dataset'
arch=('any')
url='https://github.com/lvis-dataset/lvis-api'
license=('BSD')
depends=(
  python-opencv
  python-cycler
  python-dateutil
  python-kiwisolver
  python-matplotlib
  python-numpy
  python-pyparsing
  python-pycocotools
  python-six
)
makedepends=(
  git
  cython
  python-pip
  python-setuptools
)
checkdepends=(
  hdf5
  qt5-base
)
provides=(python-lvis)
conflicts=(python-lvis)

source=("${_pkgname}::git+https://github.com/lvis-dataset/lvis-api.git")
sha512sums=('SKIP')

pkgver() {
  cd "${_pkgname}"
  printf "%s.r%s.%s" "${_pkgver}" "$(git rev-list --count HEAD)" "$(git rev-parse --short HEAD)"
}

build() {
  cd "${_pkgname}"
  python setup.py build
}

check() {
  cd "${_pkgname}"
  python test.py
}

package() {
  cd "${_pkgname}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 "LICENSE" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
