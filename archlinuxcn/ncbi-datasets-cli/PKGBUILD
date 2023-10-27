# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=datasets
pkgname=ncbi-datasets-cli
pkgver=15.25.0
pkgrel=1
pkgdesc='An experimental resource for finding and building datasets across NCBI databases'
arch=('x86_64')
url='https://github.com/ncbi/datasets'
license=('custom')
source=("${pkgname}-${pkgver}.zip::https://github.com/ncbi/datasets/releases/download/v${pkgver}/linux-amd64.cli.package.zip"
        "${pkgname}-${pkgver}.tar.gz::https://github.com/ncbi/datasets/archive/refs/tags/v${pkgver}.tar.gz"
)
sha512sums=('12432e7d7dcd3fb2fc41cd2406fa6f28f2767d26c971a3aa6ff5314900b56dd3cd6deb8f50cb7f512ffaf95fe926c16ae662d653ba7e1d2adbde421acd7a18e6'
            'd987cadd96c4b50d9dc05492d6ceda9241fc26407b54c4cb2c70a1b159dfb19de1d210f154d7837a94219c96d85afc96b971b32c7fa40ab2b5e1d7bb3a06d5c4')

package() {
  install -Dm755 "datasets" "${pkgdir}/usr/bin/ncbi-datasets"
  install -Dm755 "dataformat" "${pkgdir}/usr/bin/ncbi-dataformat"

  install -Dm644 "${_pkgname}-${pkgver}/LICENSE.md" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
