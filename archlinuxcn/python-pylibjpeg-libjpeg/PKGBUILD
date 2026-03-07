# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=pylibjpeg-libjpeg
pkgname=python-pylibjpeg-libjpeg
pkgver=2.4.0
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
sha512sums=('b33f4372692edb00ba1ea413db371249590f23a8089980e5c0bb63aac100492db824eeaf43f422fa8551b8416c563cbad2d6c1871cddc9161b18da1e5ec66b4b')

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
