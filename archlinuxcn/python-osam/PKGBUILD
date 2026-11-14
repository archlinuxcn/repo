# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=osam
pkgname=python-osam
pkgver=0.11.8
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
sha512sums=('39efdd9a89f7d4e4e211bc1f59bc57bab5b44bb31afb58fec2d999fd6d4dbb248e50af1e144c8179181d33972002cbe1fed9ace356628eba8d45601d9452243c')

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
