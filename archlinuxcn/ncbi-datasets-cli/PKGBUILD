# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=datasets
pkgname=ncbi-datasets-cli
pkgver=15.22.0
pkgrel=1
pkgdesc='An experimental resource for finding and building datasets across NCBI databases'
arch=('x86_64')
url='https://github.com/ncbi/datasets'
license=('custom')
source=("${pkgname}-${pkgver}.zip::https://github.com/ncbi/datasets/releases/download/v${pkgver}/linux-amd64.cli.package.zip"
        "${pkgname}-${pkgver}.tar.gz::https://github.com/ncbi/datasets/archive/refs/tags/v${pkgver}.tar.gz"
)
sha512sums=('626c47610575e5d048c1043aafa48e5cc988150e6673bbf346407543f5f80e7ab7ff660321b974bf36db794a0f37cb0397a2f99c0eb06cd0309a9eeabdfcdb66'
            '7fbc61c1058c38e547db711ebdd324ef3e8606723f7e09f99e22c54d8ac3c0da05b48d0bee0ecbf01b292a0aac5d10b84bdd2e4b6294e1179b3dcb3a09bc3466')

package() {
  install -Dm755 "datasets" "${pkgdir}/usr/bin/ncbi-datasets"
  install -Dm755 "dataformat" "${pkgdir}/usr/bin/ncbi-dataformat"

  install -Dm644 "${_pkgname}-${pkgver}/LICENSE.md" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
