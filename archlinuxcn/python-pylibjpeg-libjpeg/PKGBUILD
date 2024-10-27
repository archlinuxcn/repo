# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=pylibjpeg-libjpeg
pkgname=python-pylibjpeg-libjpeg
pkgver=2.3.0
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
sha512sums=('2c60a1e48e77cdfa46b7d40fa5c9c251b3e29a9523d49f38cc6bbd9cf9935ac28f0a4277d7090db923915c700801288ae96358ca5ef2e963b69491afd5d69748')

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
