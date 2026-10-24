# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=pylibjpeg-libjpeg
pkgname=python-pylibjpeg-libjpeg
pkgver=2.5.0
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
sha512sums=('cd74edf6a7a2fd6fc6b046c40cdbf9ec5548008bd4d861b74c988990fa3ddde91bcda7488f753df26bcdb1b0f2d2c00775d80f24b9408b17dabfcee8094a3786')

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
