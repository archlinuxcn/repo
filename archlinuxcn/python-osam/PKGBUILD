# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=osam
pkgname=python-osam
pkgver=0.9.6
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
sha512sums=('8dc25714ec373a477d85a99f313bff624d92341b2ab8c22114d24e921cf942d9ed684a13537ce003af7252046d4b956549869d12fc5af1bb79062f504cb59c02')

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
