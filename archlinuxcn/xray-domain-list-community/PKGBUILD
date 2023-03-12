# Maintainer: Dct Mei <dctxmei@yandex.com>
# Contributor: Felix Yan <felixonmars@archlinux.org>

pkgname=xray-domain-list-community
pkgver=20230312104722
pkgrel=1
pkgdesc="A list of domains to be used as geosites for routing purpose in Project V"
arch=('any')
url="https://github.com/v2fly/domain-list-community"
license=('MIT')
makedepends=('go')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz")
sha256sums=('f8919ba977a333bf5379a5f6cda6c6906fd4045080d98755bb57e7d5f9f187c0')

build() {
    cd "${srcdir}"/"domain-list-community-${pkgver}"/
    go run main.go
}

package() {
    cd "${srcdir}"/"domain-list-community-${pkgver}"/
    install -Dm 644 dlc.dat "${pkgdir}"/usr/share/xray/geosite.dat
    install -Dm 644 "${srcdir}"/"domain-list-community-${pkgver}"/LICENSE -t "${pkgdir}"/usr/share/licenses/"$pkgname"/
}
