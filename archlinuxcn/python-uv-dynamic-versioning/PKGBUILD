# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=uv-dynamic-versioning
pkgname=python-uv-dynamic-versioning
pkgver=0.10.0
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
sha512sums=('6e1fb4840764d7f520007c8140590ef6fb6b7941e710609d8ebd494b3964a1482da80c14f6843382472da054587905b0311bff102995c468276ef5c1ea3d4092')

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
