# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=pylibjpeg-libjpeg
pkgname=python-pylibjpeg-libjpeg
pkgver=2.1.1
pkgrel=1
epoch=1
pkgdesc='A JPEG, JPEG-LS and JPEG XT plugin for pylibjpeg'
arch=('x86_64')
url='https://github.com/pydicom/pylibjpeg-libjpeg'
license=('GPL-3.0-or-later')
depends=(
  gcc-libs
  glibc
  python-numpy
)
makedepends=(
  git
  poetry
  python-installer
)
source=("${pkgname}::git+https://github.com/pydicom/pylibjpeg-libjpeg.git#tag=v${pkgver}")
sha512sums=('5bf8c3c6946ae129bfe180014ee187848405247d7b9cc8d83e17d9a1266a4435038e04c572221620464f28da1bbe4cc4310addeea1e7619beb9319c910a982f2')

prepare() {
  cd "${pkgname}"
  git submodule update --init --recursive
}

build() {
  cd "${pkgname}"
  poetry build --format wheel
}

package() {
  cd "${pkgname}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  local site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  rm -rf "${pkgdir}${site_packages}/libjpeg/tests"
}
# vim:set ts=2 sw=2 et:
