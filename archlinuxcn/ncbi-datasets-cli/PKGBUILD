# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=datasets
pkgname=ncbi-datasets-cli
pkgver=13.42.1
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
sha512sums=('01760681c75462ef2654dce579e645de637eb08f405c8bf9d48c944d738a84f39af7b0cfed53a3d5b0bd16d00209c35140c2d4b52d2f640742bc21572851d5d9')

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
