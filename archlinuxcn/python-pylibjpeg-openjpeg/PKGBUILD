# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=pylibjpeg-openjpeg
pkgname=python-pylibjpeg-openjpeg
pkgver=1.0.1
pkgrel=1
pkgdesc='A J2K and JP2 plugin for pylibjpeg'
arch=('x86_64')
url='https://github.com/pydicom/pylibjpeg-openjpeg'
license=(MIT)
depends=(
  python-numpy
)
makedepends=(
  cmake
  cython
  git
)
source=("${pkgname}::git+https://github.com/pydicom/pylibjpeg-openjpeg.git#tag=v1.0.1")
sha512sums=('SKIP')

get_pyver() {
  python -c 'import sys; print(str(sys.version_info[0]) + "." + str(sys.version_info[1]))'
}

prepare() {
  cd "${pkgname}"
  git submodule update --init --recursive
}

build() {
  cd "${pkgname}"
  python setup.py build
}

package() {
  cd "${pkgname}"
  python setup.py install --root="${pkgdir}" --optimize=1 --skip-build
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
  rm -rf "${pkgdir}/usr/lib/python$(get_pyver)/site-packages/openjpeg/src"
}
# vim:set ts=2 sw=2 et:
