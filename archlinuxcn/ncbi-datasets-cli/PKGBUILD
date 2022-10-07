# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=datasets
pkgname=ncbi-datasets-cli
pkgver=13.43.2
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
sha512sums=('ba143959d898dfb0cfabad8ee336c9cfbf9e7ffab6d1287a1e8ed9d53279fe87c96f0e004cd8386efd96f8d229baa8c44f74118373ff2ecc5346a344bd37ab6d')

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
