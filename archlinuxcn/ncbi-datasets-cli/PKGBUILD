# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=datasets
pkgname=ncbi-datasets-cli
pkgver=14.8.1
pkgrel=1
pkgdesc='An experimental resource for finding and building datasets across NCBI databases'
arch=('x86_64')
url='https://github.com/ncbi/datasets'
license=('custom')
source=("${pkgname}-${pkgver}.zip::https://github.com/ncbi/datasets/releases/download/v${pkgver}/linux-amd64.cli.package.zip"
        "${pkgname}-${pkgver}.tar.gz::https://github.com/ncbi/datasets/archive/refs/tags/v${pkgver}.tar.gz"
)
sha512sums=('d9d3ae3d5a94b179c74781eb5a8be8ca6e08de5ccaf93b258e6f5cd78dd8f8148c79747797d5cc5ca009a3375d85b3e4a90a9f2142ef1fd72248d9c8a55a3063'
            'b302118e3161e6cfa5f21b9b3677b373567c83e1dfbc5874fcadf2c7043304a56d8d9852422261386e7a46b7f4335a5a3ba8f27f11e2fa422ccaa2a648f45a3b')

package() {
  install -Dm755 "datasets" "${pkgdir}/usr/bin/ncbi-datasets"
  install -Dm755 "dataformat" "${pkgdir}/usr/bin/ncbi-dataformat"

  install -Dm644 "${_pkgname}-${pkgver}/LICENSE.md" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
