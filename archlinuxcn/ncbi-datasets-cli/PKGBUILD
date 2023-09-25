# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=datasets
pkgname=ncbi-datasets-cli
pkgver=15.20.0
pkgrel=1
pkgdesc='An experimental resource for finding and building datasets across NCBI databases'
arch=('x86_64')
url='https://github.com/ncbi/datasets'
license=('custom')
source=("${pkgname}-${pkgver}.zip::https://github.com/ncbi/datasets/releases/download/v${pkgver}/linux-amd64.cli.package.zip"
        "${pkgname}-${pkgver}.tar.gz::https://github.com/ncbi/datasets/archive/refs/tags/v${pkgver}.tar.gz"
)
sha512sums=('2c4089b51b59009fe7087f3e45eb0e1df061185d2ec7b664432c03af0365a5d584a3f41766fb3762eb5fc41c9e9604721daf6bc2a89a632764ee9809faec5f18'
            '29b71ddb362635e305ece9d712ba28fdbe06c65abde652f5c2b6e4c00e448acb87f09ee6d422a30835c24ea44faf09248ad4e1c871c2496aeda0cf6dae754c0f')

package() {
  install -Dm755 "datasets" "${pkgdir}/usr/bin/ncbi-datasets"
  install -Dm755 "dataformat" "${pkgdir}/usr/bin/ncbi-dataformat"

  install -Dm644 "${_pkgname}-${pkgver}/LICENSE.md" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
