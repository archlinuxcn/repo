# Maintainer: Dct Mei <dctxmei@yandex.com>

pkgname=clash-geoip
_pkgname=maxmind-geoip
pkgver=20230212
pkgrel=1
pkgdesc="A GeoLite2 data created by MaxMind"
arch=('any')
url="https://github.com/Dreamacro/maxmind-geoip"
license=('custom')
source=("${_pkgname}-${pkgver}.mmdb::${url}/releases/download/${pkgver}/Country.mmdb")
sha256sums=('4e799aeada444f856b9b91bc2a62e9b159e90f62482adb39ea4650b0121b459f')

package() {
    install -Dm0644 "${_pkgname}-${pkgver}.mmdb" "${pkgdir}"/etc/clash/Country.mmdb
}
