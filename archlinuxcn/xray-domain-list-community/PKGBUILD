# Maintainer: Dct Mei <dctxmei@yandex.com>
# Contributor: Felix Yan <felixonmars@archlinux.org>

pkgname=xray-domain-list-community
pkgver=20220831082552
pkgrel=1
pkgdesc="A list of domains to be used as geosites for routing purpose in Project V"
arch=('any')
url="https://github.com/v2fly/domain-list-community"
license=('MIT')
makedepends=('go')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz")
sha256sums=('98920034759b895850ec4bc0da6f3eb2c17719b0a728fcf47eb9cad52c87f999')

build() {
    cd "${srcdir}"/"domain-list-community-${pkgver}"/
    go run main.go
}

package() {
    cd "${srcdir}"/"domain-list-community-${pkgver}"/
    install -Dm 644 dlc.dat "${pkgdir}"/usr/share/xray/geosite.dat
    install -Dm 644 "${srcdir}"/"domain-list-community-${pkgver}"/LICENSE -t "${pkgdir}"/usr/share/licenses/"$pkgname"/
}
