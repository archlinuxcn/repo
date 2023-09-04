# Maintainer: Dct Mei <dctxmei@yandex.com>

pkgname=yacd-meta
_pkgname=Yacd-meta
pkgver=0.3.6
pkgrel=1
pkgdesc="Yet Another Clash Dashboard"
arch=('any')
url="https://github.com/MetaCubeX/Yacd-meta"
license=('unknown')
depends=('clash-meta')
makedepends=('yarn')
conflicts=('yacd-meta-git')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")
sha256sums=('1585fbf7c546cf15a5465044135c32af3804c38cf1577295ee06d7416c3b0555')

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
