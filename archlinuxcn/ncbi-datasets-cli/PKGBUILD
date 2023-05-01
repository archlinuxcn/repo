# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=datasets
pkgname=ncbi-datasets-cli
pkgver=14.25.2
pkgrel=1
pkgdesc='An experimental resource for finding and building datasets across NCBI databases'
arch=('x86_64')
url='https://github.com/ncbi/datasets'
license=('custom')
source=("${pkgname}-${pkgver}.zip::https://github.com/ncbi/datasets/releases/download/v${pkgver}/linux-amd64.cli.package.zip"
        "${pkgname}-${pkgver}.tar.gz::https://github.com/ncbi/datasets/archive/refs/tags/v${pkgver}.tar.gz"
)
sha512sums=('e49507a8495f5932ac650f28c54bc9c3fd476999e84b6f2d4a47817bdd83d04dfdce7d8923eaf3ef4e29412c6d0caf7c2ca19a3651d64f04e068caf9413510d0'
            'fb0ca34a68f23aca4093750b9e130dcdb305e1543e1144652254be096b3e2697a4241f17a49942614009377cbb161fb0c1c4b295c183ce157ea2890af451958e')

package() {
  install -Dm755 "datasets" "${pkgdir}/usr/bin/ncbi-datasets"
  install -Dm755 "dataformat" "${pkgdir}/usr/bin/ncbi-dataformat"

  install -Dm644 "${_pkgname}-${pkgver}/LICENSE.md" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
