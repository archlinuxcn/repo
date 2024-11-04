# Maintainer: Dct Mei <dctxmei@yandex.com>

pkgname=clash-geoip
pkgver=202411041511
pkgrel=1
pkgdesc="GeoIP files for Clash"
arch=(any)
url="https://github.com/Loyalsoldier/geoip"
license=(CC-BY-SA-4.0 GPL-3.0-or-later)
source=("${pkgname}-${pkgver}.mmdb::${url}/releases/download/${pkgver}/Country.mmdb")
sha256sums=('6f7bcf065758c3248d1b8c69114cbd54091dc9c029596ec53ca6057ce52df23c')

package() {
    install -Dm0644 "${pkgname}-${pkgver}.mmdb" "${pkgdir}/etc/clash/Country.mmdb"
}
