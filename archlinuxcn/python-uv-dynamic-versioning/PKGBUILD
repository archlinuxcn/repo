# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=uv-dynamic-versioning
pkgname=python-uv-dynamic-versioning
pkgver=0.14.0
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
sha512sums=('d5a5ca2d727721f346cc6396e4b3ca46678e72da18797e47201ac30298c64117c468f40107af779720c641020db8c0d81964bef9df26462a1205e016bde4990d')

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
