# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=osam
pkgname=python-osam
pkgver=0.4.0
pkgrel=1
pkgdesc='A tool to run open-source promptable vision models locally'
arch=('any')
url='https://github.com/wkentaro/osam'
license=('MIT')
depends=(
  gdown
  python-click
  python-imgviz
  python-loguru
  python-onnxruntime
  python-pillow
  python-pydantic
)
makedepends=(
  python-build
  python-installer
  python-hatchling
  python-hatch-fancy-pypi-readme
  python-hatch-vcs
  python-wheel
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/wkentaro/osam/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('5fb86627b043feb0e1e715894efc932cda0d630ad6ab5a1b7170715d70d11925aa908bae616338b2025bfce3fb0b56f204601cf879283869157ac952baacd689')

build() {
  cd "${_pkgname}-${pkgver}"
  SETUPTOOLS_SCM_PRETEND_VERSION=${pkgver} \
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
