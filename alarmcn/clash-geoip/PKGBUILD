# Maintainer: pngdeity <pngdeity@tutanota.com>
# Contributor: willker <wz dot willker at gmail dot com>
# Contributor: celeste <renzhewudi2013@outlook.com>

_githubname="Loyalsoldier/geoip"

pkgname=clash-geoip
changelog=clash-geoip.changelog
pkgver=202606182327
pkgrel=1
pkgdesc="GeoIP files for Clash"
arch=(any)
url="https://github.com/Loyalsoldier/geoip"
license=(CC-BY-SA-4.0 GPL-3.0-or-later)
source=(
    "${pkgname}-${pkgver}.mmdb::${url}/releases/download/${pkgver}/Country.mmdb"
)
sha256sums=('3cdca3b21dc247ad62df291d36b5117b054089cd006e4342bde37e0c2cd0e7f3')

package() {
    install -Dm0644 "${pkgname}-${pkgver}.mmdb" "${pkgdir}/etc/clash/Country.mmdb"
}
