# Maintainer: Dct Mei <dctxmei@yandex.com>
# Contributor: Felix Yan <felixonmars@archlinux.org>

pkgname=xray-geoip
pkgver=202208040058
pkgrel=1
pkgdesc="GeoIP List for Xray"
arch=('any')
url="https://github.com/v2fly/geoip"
license=('CCPL:by-sa')
source=("geoip-${pkgver}.dat::${url}/releases/download/${pkgver}/geoip.dat"
        "${url}/raw/master/LICENSE")
sha256sums=('9b889b14befba1fa0c4c8da9ffab1e23749a132dfdd0b60c672e89624c9e5ae1'
            '5e436ff8ffbb77d8607220e9bce20c8915d860010feeb6c1ebef5a85688e9b39')

package() {
    install -Dm 644 "geoip-${pkgver}.dat" "${pkgdir}"/usr/share/xray/geoip.dat
    install -Dm 644 LICENSE -t "${pkgdir}"/usr/share/licenses/xray-geoip/
}
