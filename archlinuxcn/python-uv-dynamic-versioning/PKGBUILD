# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=uv-dynamic-versioning
pkgname=python-uv-dynamic-versioning
pkgver=0.11.0
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
sha512sums=('fe614d0e1bbf2264438c3044400776e0f4f56461f93db33ddbef45b1940f31deba0e31f92e70a12d3a345d7dc24fc1dfbeef6f50f6825436098e2caa9970d0b1')

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
