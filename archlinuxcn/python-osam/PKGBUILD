# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=osam
pkgname=python-osam
pkgver=0.12.0
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
sha512sums=('1591de3baa1040a2d71995a9cabe32f7a8bd7965758b836eadb493238a18ddc7d5d1b82d3db348e1abc50636051e9c7ef344b0eca5a2ae171fdcb2067d62eaa7')

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
