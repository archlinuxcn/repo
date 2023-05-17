# Maintainer: Dct Mei <dctxmei@yandex.com>
# Contributor: Felix Yan <felixonmars@archlinux.org>

pkgname=v2ray-china-list
pkgver=20230517003004
pkgrel=1
pkgdesc="V2Ray deployment of felixonmars/dnsmasq-china-list project"
arch=('any')
url="https://github.com/dctxmei/v2ray-china-list"
license=('GPL3')
makedepends=('go')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz")
sha256sums=('3ced0ba000418a3cfc9356d38e95ec19a2006946b2bf3dad34d9f959ef1b9b31')

build() {
    cd "${srcdir}"/"${pkgname}-${pkgver}"/
    go run main.go
}

package() {
    cd "${srcdir}"/"${pkgname}-${pkgver}"/
    install -Dm 644 china-list.dat -t "${pkgdir}"/usr/share/v2ray/
    install -Dm 644 LICENSE -t "${pkgdir}"/usr/share/licenses/"${pkgname}"/
}
