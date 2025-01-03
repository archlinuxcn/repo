# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=xtcocoapi
pkgname=python-xtcocotools
pkgver=1.14.3
pkgrel=5
pkgdesc='Extended COCO-API'
arch=('x86_64')
url='https://github.com/jin-s13/xtcocoapi'
license=('MIT')
depends=(
  glibc
  python-numpy
  python-matplotlib
)
makedepends=(
  cython
  python-build
  python-installer
  python-setuptools
  python-wheel
)
provides=(
  python-xcocotools
)
conflicts=(
  python-xcocotools
)
replaces=(
  python-xcocotools
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/jin-s13/xtcocoapi/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('99cd46eaee88ab4eaf7154a8fa0aca7c36aafa96e9cd49b836f338884f24206fdd819dbf23931cbd51fc1aeb8c60ffed28eef77d16cb5095e56f3819643b7b8d')

prepare() {
  sed -i "s/version=get_version()/version='$pkgver'/" "${srcdir}/${_pkgname}-${pkgver}/setup.py"
}

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
