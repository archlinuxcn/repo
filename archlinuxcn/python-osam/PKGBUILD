# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=osam
pkgname=python-osam
pkgver=0.4.1
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
sha512sums=('b114a4fe03f1cac0b9b41f1ad8f9e9efcc86a31988b7fdf1d0f038bb29cb0b6f7a540453082a551f46a1ad9f8c861dbaccd28cfdcac4009fa429e4ea724aefba')

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
