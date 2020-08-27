# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-pycocotools-openmm-git
_pkgname=pycocotools
_pkgver=12.0.0
pkgver=12.0.0.r215.9fa16b4
pkgrel=1
pkgdesc='Official APIs for the MS-COCO dataset (openmm lab fork)'
arch=(x86_64)
url='https://github.com/open-mmlab/cocoapi'
license=(BSD)
depends=(
  python-matplotlib
  python-numpy
)
makedepends=(
  cython
  git
  python-setuptools
)
provides=(python-pycocotools python-pycocotools-openmm)
conflicts=(python-pycocotools python-pycocotools-openmm)

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
