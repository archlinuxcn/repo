# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=pylibjpeg-openjpeg
pkgname=python-pylibjpeg-openjpeg
pkgver=2.3.0
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
  git
  poetry
  python-installer
)
source=("${pkgname}-${pkgver}::git+https://github.com/pydicom/pylibjpeg-openjpeg.git#tag=v${pkgver}")
sha512sums=('decc546b5d97309ac20338be0f2c4a827854991d89cd162d36dfba6a6f49f946999c3552b16f1fd7170cc0397c7d418bb1e0106dca2ec051d847e30ab7c80523')

prepare() {
  cd "${pkgname}-${pkgver}"
  git submodule update --init --recursive
}

build() {
  cd "${pkgname}-${pkgver}"
  poetry build --format wheel
}

package() {
  local site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  cd "${pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
  # remove tests files
  rm -rf "${pkgdir}${site_packages}/openjpeg/tests"
}
# vim:set ts=2 sw=2 et:
