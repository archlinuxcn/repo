# Maintainer: Dct Mei <dctxmei@yandex.com>

pkgname=clash-geoip
pkgver=202508140029
pkgrel=1
pkgdesc="GeoIP files for Clash"
arch=(any)
url="https://github.com/Loyalsoldier/geoip"
license=(CC-BY-SA-4.0 GPL-3.0-or-later)
source=("${pkgname}-${pkgver}.mmdb::${url}/releases/download/${pkgver}/Country.mmdb")
sha256sums=('1831766d7efb8f579aa2f72e55219bf13d3c3c0981afdfba4a1d74177024387f')

package() {
    install -Dm0644 "${pkgname}-${pkgver}.mmdb" "${pkgdir}/etc/clash/Country.mmdb"
}
