# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=pylibjpeg-openjpeg
pkgname=python-pylibjpeg-openjpeg
pkgver=2.6.0
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
source=("${pkgname}::git+https://github.com/pydicom/pylibjpeg-openjpeg.git#tag=v${pkgver}")
sha512sums=('d904cd07b6a85ae2986faa7c7a7678a04b397b91d0b6dc974457d514929c3491ceb9157a71d9b227e371a293adfe825d4e551ca7a2aa92799f9a6834d814a3e8')

prepare() {
  cd "${pkgname}"
  git submodule update --init --recursive
}

build() {
  cd "${pkgname}"
  poetry build --format wheel
}

package() {
  local site_packages=$(python -c "import site; print(site.getsitepackages()[0])")
  cd "${pkgname}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
  # remove tests files
  rm -rf "${pkgdir}${site_packages}/openjpeg/tests"
}
# vim:set ts=2 sw=2 et:
