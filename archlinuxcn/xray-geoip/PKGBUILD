# Maintainer: Dct Mei <dctxmei@yandex.com>
# Contributor: Felix Yan <felixonmars@archlinux.org>

pkgname=xray-geoip
pkgver=202107010026
pkgrel=1
pkgdesc="GeoIP List for Xray"
arch=('any')
url="https://github.com/v2fly/geoip"
license=('CCPL:by-sa')
source=("geoip-${pkgver}.dat::${url}/releases/download/${pkgver}/geoip.dat"
        "${url}/raw/master/LICENSE")
sha256sums=('8c3e0c2aa114c31631c0df209f8426bdff04b664f383b4decc988b642fe1bc5b'
            '5e436ff8ffbb77d8607220e9bce20c8915d860010feeb6c1ebef5a85688e9b39')

package() {
    install -Dm 644 "geoip-${pkgver}.dat" "${pkgdir}"/usr/share/xray/geoip.dat
    install -Dm 644 LICENSE -t "${pkgdir}"/usr/share/licenses/xray-geoip/
}
