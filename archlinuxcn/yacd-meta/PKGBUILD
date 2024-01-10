# Maintainer: Dct Mei <dctxmei@yandex.com>

pkgname=yacd-meta
_pkgname=Yacd-meta
pkgver=0.3.7
pkgrel=2
pkgdesc="Yet Another Clash Dashboard"
arch=('any')
url="https://github.com/MetaCubeX/Yacd-meta"
license=('unknown')
makedepends=('yarn')
optdepends=('clash-meta')
conflicts=('yacd-meta-git')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")
sha256sums=('098ed76836c41778ecb9707bf9a5c77f77eaa1d6c63300d5edeac34339cb5f87')

build() {
    cd "${srcdir}"/"${_pkgname}-${pkgver}"/
    yarn cache clean
    yarn install
    yarn build
}

package() {
    cd "${srcdir}"/"${_pkgname}-${pkgver}"/
    #install -Dm 644 LICENSE -t "${pkgdir}"/usr/share/licenses/"${pkgname}"/
    cd public/
    find . -type d -exec install -vd "${pkgdir}"/usr/share/"${pkgname}"/{} \;
    find . -type f -exec install -vm 644 {} "${pkgdir}"/usr/share/"${pkgname}"/{} \;
}
