# Maintainer: Dct Mei <dctxmei@yandex.com>
# Contributor: Felix Yan <felixonmars@archlinux.org>

pkgname=xray-geoip
pkgver=202407110044
pkgrel=1
pkgdesc="GeoIP List for Xray"
arch=('any')
url="https://github.com/v2fly/geoip"
license=('CCPL:by-sa')
source=("geoip-${pkgver}.dat::${url}/releases/download/${pkgver}/geoip.dat"
        "${url}/raw/master/LICENSE")
sha256sums=('83c8d38a4fff932fcbfe726c1f85c0debb1bf169afcfa18566c731a2f2c1f7b6'
            '5e436ff8ffbb77d8607220e9bce20c8915d860010feeb6c1ebef5a85688e9b39')

package() {
    install -Dm 644 "geoip-${pkgver}.dat" "${pkgdir}"/usr/share/xray/geoip.dat
    install -Dm 644 LICENSE -t "${pkgdir}"/usr/share/licenses/xray-geoip/
}
