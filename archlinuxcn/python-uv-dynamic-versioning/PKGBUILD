# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=uv-dynamic-versioning
pkgname=python-uv-dynamic-versioning
pkgver=0.12.0
pkgrel=1
pkgdesc='PDynamic versioning based on VCS tags for uv/hatch project'
arch=(any)
url='https://github.com/ninoseki/uv-dynamic-versioning'
license=(MIT)
depends=(
  python-tomlkit
  python-pydantic
  python-jinja
  python-hatchling
  python-dunamai
)

makedepends=(
  python-build
  python-installer
  python-wheel
)

source=(
  "${_pkgname}-${pkgver}.tar.gz::https://github.com/ninoseki/uv-dynamic-versioning/archive/refs/tags/v${pkgver}.tar.gz"
)
sha512sums=('9b912ff37a417dcb5a616572337f841b62adc9443d1de8e09ae1213e1b5262b8da6d131f976ef78ce59eccd496c7b66a9d3b42f89e9ca1f4d988818cf7730dfd')

build() {
  cd "${_pkgname}-${pkgver}"
  python -m build --wheel --no-isolation
}

package() {
  cd "${_pkgname}-${pkgver}"
  python -m installer --destdir="${pkgdir}" dist/*.whl
  install -Dm644 LICENSE -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
