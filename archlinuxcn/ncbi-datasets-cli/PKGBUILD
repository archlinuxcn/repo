# Maintainer: Butui Hu <hot123tea123@gmail.com>

_pkgname=datasets
pkgname=ncbi-datasets-cli
pkgver=15.13.1
pkgrel=1
pkgdesc='An experimental resource for finding and building datasets across NCBI databases'
arch=('x86_64')
url='https://github.com/ncbi/datasets'
license=('custom')
source=("${pkgname}-${pkgver}.zip::https://github.com/ncbi/datasets/releases/download/v${pkgver}/linux-amd64.cli.package.zip"
        "${pkgname}-${pkgver}.tar.gz::https://github.com/ncbi/datasets/archive/refs/tags/v${pkgver}.tar.gz"
)
sha512sums=('e129c6a7caed583ef3ab6a3bd34965e9b0be44e9996f7e425e6472147603267c347806dcdb6c3e04cbcb1a208f1a84859a4043a6bab477bae0782d5c08e60a3a'
            '764a9765a5e0a1af1d9b9867fae75a66a8caa8cf16f39bcb17d6644cb6db39cfcf575c7b5e5d9ee598880f0f9ba8b774f4b826c6b253aa0f25c16ffd96d03ac7')

package() {
  install -Dm755 "datasets" "${pkgdir}/usr/bin/ncbi-datasets"
  install -Dm755 "dataformat" "${pkgdir}/usr/bin/ncbi-dataformat"

  install -Dm644 "${_pkgname}-${pkgver}/LICENSE.md" -t "${pkgdir}/usr/share/licenses/${pkgname}"
}
# vim:set ts=2 sw=2 et:
