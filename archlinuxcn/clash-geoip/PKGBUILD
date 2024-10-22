# Maintainer: Dct Mei <dctxmei@yandex.com>

pkgname=clash-geoip
pkgver=202410221049
pkgrel=1
pkgdesc="GeoIP files for Clash"
arch=(any)
url="https://github.com/Loyalsoldier/geoip"
license=(CC-BY-SA-4.0 GPL-3.0-or-later)
source=("${pkgname}-${pkgver}.mmdb::${url}/releases/download/${pkgver}/Country.mmdb")
sha256sums=('dbf75bc677a7e7a3faa2866f41a068dd671929d800b5eb217bf64a6c0b94feea')

package() {
    install -Dm0644 "${pkgname}-${pkgver}.mmdb" "${pkgdir}/etc/clash/Country.mmdb"
}
