# Maintainer: Dct Mei <dctxmei@yandex.com>
# Contributor: Felix Yan <felixonmars@archlinux.org>

pkgname=v2ray-china-list
pkgver=20250326003840
pkgrel=1
pkgdesc="V2Ray deployment of felixonmars/dnsmasq-china-list project"
arch=('any')
url="https://github.com/dctxmei/v2ray-china-list"
license=('GPL3')
makedepends=('go')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz")
sha256sums=('d6055dfb9e10ff172ccfcae9c11e9bbbb7da06f4a5a40f78e7aa0f97250ba365')

build() {
    cd "${srcdir}"/"${pkgname}-${pkgver}"/
    go run main.go
}

package() {
    cd "${srcdir}"/"${pkgname}-${pkgver}"/
    install -Dm 644 china-list.dat -t "${pkgdir}"/usr/share/v2ray/
    install -Dm 644 LICENSE -t "${pkgdir}"/usr/share/licenses/"${pkgname}"/
}
