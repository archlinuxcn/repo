# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=datasets
pkgname=ncbi-datasets-cli
pkgver=13.43.1
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
sha512sums=('d42cf1dcaad2467f1c03a4909c84c95b57a1e8a548ef643ad94598ef1c0e3da47203c616f7a1a65c5eb3e494d02f654c6b63cb0319a39cf9ca6a81dc2a5c0d0a')

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
