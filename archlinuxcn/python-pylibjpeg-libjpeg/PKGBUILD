# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=pylibjpeg-libjpeg
pkgname=python-pylibjpeg-libjpeg
pkgver=2.02
pkgrel=1
pkgdesc='A JPEG, JPEG-LS and JPEG XT plugin for pylibjpeg'
arch=('x86_64')
url='https://github.com/pydicom/pylibjpeg-libjpeg'
license=(GPL)
depends=(
  python-numpy
)
makedepends=(
  git
  poetry
  python-installer
)
source=("${pkgname}::git+https://github.com/pydicom/pylibjpeg-libjpeg.git#tag=v${pkgver}")
sha512sums=('SKIP')

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
