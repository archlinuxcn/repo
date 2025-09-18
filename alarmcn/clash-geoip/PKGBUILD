# Maintainer: Dct Mei <dctxmei@yandex.com>

pkgname=clash-geoip
pkgver=202509180019
pkgrel=1
pkgdesc="GeoIP files for Clash"
arch=(any)
url="https://github.com/Loyalsoldier/geoip"
license=(CC-BY-SA-4.0 GPL-3.0-or-later)
source=("${pkgname}-${pkgver}.mmdb::${url}/releases/download/${pkgver}/Country.mmdb")
sha256sums=('577a545e33aa6375d844e28c7becc6f57f40ed435b25cf3687616846ae4f7644')

package() {
    install -Dm0644 "${pkgname}-${pkgver}.mmdb" "${pkgdir}/etc/clash/Country.mmdb"
}
