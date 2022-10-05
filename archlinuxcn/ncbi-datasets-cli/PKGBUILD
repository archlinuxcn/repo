# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=datasets
pkgname=ncbi-datasets-cli
pkgver=13.43.0
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
sha512sums=('180321070af1c7d664908195d9c9a3b0a4abac18ca51d079bbda6772c89af591265c84f5ae7d6f20c0deabaf01a8956c687a20b69b8aa01271df4838e7e75795')

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
