# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=datasets
pkgname=ncbi-datasets-cli
pkgver=16.3.0
pkgrel=1
pkgdesc='An experimental resource for finding and building datasets across NCBI databases'
arch=('x86_64')
url='https://github.com/ncbi/datasets'
license=('custom')
source=("${pkgname}-${pkgver}.zip::https://github.com/ncbi/datasets/releases/download/v${pkgver}/linux-amd64.cli.package.zip"
        "${pkgname}-${pkgver}.tar.gz::https://github.com/ncbi/datasets/archive/refs/tags/v${pkgver}.tar.gz"
)
sha512sums=('cb7e99073d6aaeb7f72de79cf051f9098cd5012c0ba67b3adaa21f9d10a0917c94e859bbc2ba79b794ea834bcf616dfc36f5319f0c3d8ac8cb24abe74a3f14bd'
            '17e1f87f4f7082355bf89193b85323f2eb19c37ae122843cd12788b1ae9d1b09ade474ca215de0d2f7769a3be448c44506dd08ebac4aafc375218d0ddcdf58d2')

package() {
  install -Dm755 "datasets" "${pkgdir}/usr/bin/ncbi-datasets"
  install -Dm755 "dataformat" "${pkgdir}/usr/bin/ncbi-dataformat"

  install -Dm644 "${_pkgname}-${pkgver}/LICENSE.md" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
