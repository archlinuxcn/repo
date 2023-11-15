# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=datasets
pkgname=ncbi-datasets-cli
pkgver=15.28.0
pkgrel=1
pkgdesc='An experimental resource for finding and building datasets across NCBI databases'
arch=('x86_64')
url='https://github.com/ncbi/datasets'
license=('custom')
source=("${pkgname}-${pkgver}.zip::https://github.com/ncbi/datasets/releases/download/v${pkgver}/linux-amd64.cli.package.zip"
        "${pkgname}-${pkgver}.tar.gz::https://github.com/ncbi/datasets/archive/refs/tags/v${pkgver}.tar.gz"
)
sha512sums=('f5a912d3d7c54311c1e1eaa80cb61f4419d8594e4c9ba66dd7df21e92f13ddb8203a410fe9c1847b0cd3b1ffbc10e8b60bdd2ffd4be68b41fa17aaa34663d092'
            '826b74f61a4a09b4ea297af90424411b19ecd37622b60e5d9ec7c0f0a8697502ea52a2ca97198b375abb20bb2e74b04c1dfa4b9e67ac7362e6d723989774e729')

package() {
  install -Dm755 "datasets" "${pkgdir}/usr/bin/ncbi-datasets"
  install -Dm755 "dataformat" "${pkgdir}/usr/bin/ncbi-dataformat"

  install -Dm644 "${_pkgname}-${pkgver}/LICENSE.md" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
