# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=datasets
pkgname=ncbi-datasets-cli
pkgver=13.42.2
pkgrel=1
pkgdesc='An experimental resource for finding and building datasets across NCBI databases'
arch=('x86_64')
url='https://github.com/ncbi/datasets'
license=('custom')
depends=(
  glibc
)
makedepends=(
  bazel
)
source=("${_pkgname}-${pkgver}.tar.gz::https://github.com/ncbi/datasets/archive/refs/tags/v${pkgver}.tar.gz")
sha512sums=('c7e31c5721023b86d2d8f0e419cefab1e0ec073ada73caab4575bdf2f2581c0e2ba371b52cde44357a8b4b255ba4525b7f12508a92885e29c6705164dcaa688f')

build() {
  cd "${_pkgname}-${pkgver}/pkgs/ncbi-datasets-cli"
  JAVA_HOME=/usr/lib/jvm/default bazel build src/...
}

package() {
  install -Dm755 "${_pkgname}-${pkgver}/pkgs/ncbi-datasets-cli/bazel-bin/src/datasets_/datasets" "${pkgdir}/usr/bin/ncbi-datasets"
  install -Dm755 "${_pkgname}-${pkgver}/pkgs/ncbi-datasets-cli/bazel-bin/src/dataformat_/dataformat" "${pkgdir}/usr/bin/ncbi-dataformat"

  install -Dm644 "${_pkgname}-${pkgver}/pkgs/ncbi-datasets-cli/LICENSE.md" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
