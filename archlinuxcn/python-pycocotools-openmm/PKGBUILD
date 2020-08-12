# Maintainer: Butui Hu <hot123tea123@gmail.com>

pkgname=python-pycocotools-openmm
_pkgname=pycocotools
pkgver=12.0.0
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
provides=(python-pycocotools)
conflicts=(python-pycocotools)

source=("${_pkgname}::git+https://github.com/open-mmlab/cocoapi.git")
sha512sums=('SKIP')

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
