# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=datasets
pkgname=ncbi-datasets-cli
pkgver=16.4.8
pkgrel=1
pkgdesc='An experimental resource for finding and building datasets across NCBI databases'
arch=('x86_64')
url='https://github.com/ncbi/datasets'
license=('custom')
source=("${pkgname}-${pkgver}.zip::https://github.com/ncbi/datasets/releases/download/v${pkgver}/linux-amd64.cli.package.zip"
        "${pkgname}-${pkgver}.tar.gz::https://github.com/ncbi/datasets/archive/refs/tags/v${pkgver}.tar.gz"
)
sha512sums=('7aab8b4f9f3e8e2038c694dbf36942a57f772f2096323232ffb92c410cf4f14e04e9d1acf724ca99312eafc9acd90ae700b6ad2eb0d35b1f7d7ae9c66849b097'
            '67c4918edb74c5ebbc00a35baeff05bc5135cce666badd590e1082c9d8148f876b5aa51e737ac532681e9ec9a4b3c0b7c8f64b4284ad5c1d73cbd7388e99916d')

package() {
  install -Dm755 "datasets" "${pkgdir}/usr/bin/ncbi-datasets"
  install -Dm755 "dataformat" "${pkgdir}/usr/bin/ncbi-dataformat"

  install -Dm644 "${_pkgname}-${pkgver}/LICENSE.md" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
