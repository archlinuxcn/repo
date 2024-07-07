# Maintainer: Dct Mei <dctxmei@yandex.com>
# Contributor: Felix Yan <felixonmars@archlinux.org>

pkgname=v2ray-china-list
pkgver=20240707003315
pkgrel=1
pkgdesc="V2Ray deployment of felixonmars/dnsmasq-china-list project"
arch=('any')
url="https://github.com/dctxmei/v2ray-china-list"
license=('GPL3')
makedepends=('go')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz")
sha256sums=('8d02bf7cb5844c8a93aa790d8f692cb2d23c57bbb0cd48644204b66438766d38')

build() {
    cd "${srcdir}"/"${pkgname}-${pkgver}"/
    go run main.go
}

package() {
    cd "${srcdir}"/"${pkgname}-${pkgver}"/
    install -Dm 644 china-list.dat -t "${pkgdir}"/usr/share/v2ray/
    install -Dm 644 LICENSE -t "${pkgdir}"/usr/share/licenses/"${pkgname}"/
}
