# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=pylibjpeg-openjpeg
pkgname=python-pylibjpeg-openjpeg
pkgver=2.5.0
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
sha512sums=('9b11260f50d371dc193f2662925dbc8da41566f1e53bce4697e360ed109b63f4ebf129328c474c63f400203cabb64ccb46f11a8f233f9f5ff14e6ab6a14cf73e')

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
