# Maintainer: Dct Mei <dctxmei@yandex.com>
# Contributor: Felix Yan <felixonmars@archlinux.org>

pkgname=xray-geoip
pkgver=202108120026
pkgrel=1
pkgdesc="GeoIP List for Xray"
arch=('any')
url="https://github.com/v2fly/geoip"
license=('CCPL:by-sa')
source=("geoip-${pkgver}.dat::${url}/releases/download/${pkgver}/geoip.dat"
        "${url}/raw/master/LICENSE")
sha256sums=('1568a7f6865e367c52951e0b03cfe6c956b249fcf6f5732cfac98f11da1208bb'
            '5e436ff8ffbb77d8607220e9bce20c8915d860010feeb6c1ebef5a85688e9b39')

package() {
    install -Dm 644 "geoip-${pkgver}.dat" "${pkgdir}"/usr/share/xray/geoip.dat
    install -Dm 644 LICENSE -t "${pkgdir}"/usr/share/licenses/xray-geoip/
}
