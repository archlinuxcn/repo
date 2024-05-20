# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=datasets
pkgname=ncbi-datasets-cli
pkgver=16.17.1
pkgrel=1
pkgdesc='An experimental resource for finding and building datasets across NCBI databases'
arch=('x86_64')
url='https://github.com/ncbi/datasets'
license=('custom')
source=("${pkgname}-${pkgver}.zip::https://github.com/ncbi/datasets/releases/download/v${pkgver}/linux-amd64.cli.package.zip"
        "${pkgname}-${pkgver}.tar.gz::https://github.com/ncbi/datasets/archive/refs/tags/v${pkgver}.tar.gz"
)
sha512sums=('f8fbe34941b93adc4aa0459ee66b4168cb14be87e91bc46cc1d12f2c7fd819fbbf32233c5d9f5c8b4a048346f3b89a9f88318067383a8f91cdc5ef2ca53b4e5f'
            '338f87673e0b6d4fd829e0a0bb961e64c3ff86bcf342718f6e588b44445c8105ce2f25dc4042d6b38bb0a5b3eb4189c909fa5f317c4de90fb90ea7140a5d88d5')

package() {
  install -Dm755 "datasets" "${pkgdir}/usr/bin/ncbi-datasets"
  install -Dm755 "dataformat" "${pkgdir}/usr/bin/ncbi-dataformat"

  install -Dm644 "${_pkgname}-${pkgver}/LICENSE.md" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
