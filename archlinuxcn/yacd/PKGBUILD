# Maintainer: Dct Mei <dctxmei@yandex.com>

pkgname=yacd
pkgver=0.3.0
pkgrel=1
pkgdesc="Yet Another Clash Dashboard"
arch=('any')
url="https://github.com/haishanh/yacd"
license=('unknown')
depends=('clash')
makedepends=('yarn')
conflicts=('yacd-git')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/v${pkgver}.tar.gz")
sha256sums=('d1bc6ced8adb9f2871b3eff35c65beb1d0185894730ed62f016e2d21fb6337ec')

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
