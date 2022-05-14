# Maintainer: Dct Mei <dctxmei@yandex.com>

pkgname=yacd
pkgver=0.3.5
pkgrel=1
pkgdesc="Yet Another Clash Dashboard"
arch=('any')
url="https://github.com/haishanh/yacd"
license=('unknown')
depends=('clash')
makedepends=('yarn')
conflicts=('yacd-git')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")
sha256sums=('c5ae0aaa480599380bc0d7148d5fa2f305819bc88bc7f178b0b940d73cde20d5')

build() {
    cd "${srcdir}"/"${pkgname}-${pkgver}"/
    yarn cache clean
    yarn install
    yarn build
}

package() {
    cd "${srcdir}"/"${pkgname}-${pkgver}"/
    #install -Dm 644 LICENSE -t "${pkgdir}"/usr/share/licenses/"${pkgname}"/
    cd public/
    find . -type d -exec install -vd "${pkgdir}"/usr/share/"${pkgname}"/{} \;
    find . -type f -exec install -vm 644 {} "${pkgdir}"/usr/share/"${pkgname}"/{} \;
}
