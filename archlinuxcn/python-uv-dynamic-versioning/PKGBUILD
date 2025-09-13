# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=uv-dynamic-versioning
pkgname=python-uv-dynamic-versioning
pkgver=0.11.1
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
sha512sums=('c75a66a0c86871f72235023025453bc6de67235abbf81e83b9372ff48a4945e7d25135207a6a8d6b353cf9ee0927b785cc9d732f12e01c0487509f46eefe5ff4')

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
