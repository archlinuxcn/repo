# Maintainer: Dct Mei <dctxmei@yandex.com>
# Contributor: Felix Yan <felixonmars@archlinux.org>

pkgname=xray-domain-list-community
pkgver=20231223093928
pkgrel=1
pkgdesc="A list of domains to be used as geosites for routing purpose in Project V"
arch=('any')
url="https://github.com/v2fly/domain-list-community"
license=('MIT')
makedepends=('go')
source=("${pkgname}-${pkgver}.tar.gz::${url}/archive/${pkgver}.tar.gz")
sha256sums=('bf2e050f47d474b40202720b1d5293d56410309eb14576a83cbc24d9874e0a44')

build() {
    cd "${srcdir}"/"domain-list-community-${pkgver}"/
    go run main.go
}

package() {
    cd "${srcdir}"/"domain-list-community-${pkgver}"/
    install -Dm 644 dlc.dat "${pkgdir}"/usr/share/xray/geosite.dat
    install -Dm 644 "${srcdir}"/"domain-list-community-${pkgver}"/LICENSE -t "${pkgdir}"/usr/share/licenses/"$pkgname"/
}
