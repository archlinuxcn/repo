# Maintainer: Dct Mei <dctxmei@yandex.com>

pkgname=yacd
pkgver=0.3.8
pkgrel=2
pkgdesc="Yet Another Clash Dashboard"
arch=('any')
url="https://github.com/haishanh/yacd"
license=('MIT')
makedepends=('yarn')
optdepends=('clash')
conflicts=('yacd-git')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")
sha256sums=('290e23a1a2f68ab2c8a20b33e414b8abef2d6730cc3221ed62d3b173d3ce2a56')

build() {
    cd "${srcdir}"/"${pkgname}-${pkgver}"/
    yarn cache clean
    yarn install
    yarn build
}

package() {
    cd "${srcdir}"/"${pkgname}-${pkgver}"/
    install -Dm 644 LICENSE -t "${pkgdir}"/usr/share/licenses/"${pkgname}"/
    cd public/
    find . -type d -exec install -vd "${pkgdir}"/usr/share/"${pkgname}"/{} \;
    find . -type f -exec install -vm 644 {} "${pkgdir}"/usr/share/"${pkgname}"/{} \;
}
