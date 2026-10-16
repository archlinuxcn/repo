# Maintainer: pngdeity <pngdeity@tutanota.com>
# Contributor: willker <wz dot willker at gmail dot com>
# Contributor: celeste <renzhewudi2013@outlook.com>

_githubname="Loyalsoldier/geoip"

pkgname=clash-geoip
changelog=clash-geoip.changelog
pkgver=202610160207
pkgrel=1
pkgdesc="GeoIP files for Clash"
arch=(any)
url="https://github.com/Loyalsoldier/geoip"
license=(CC-BY-SA-4.0 GPL-3.0-or-later)
source=(
    "${pkgname}-${pkgver}.mmdb::${url}/releases/download/${pkgver}/Country.mmdb"
)
sha256sums=('64809d264be87ecfb7ac3ad19b7678893b6275038a7d4bf9eec72464a6c4f9fe')

package() {
    install -Dm0644 "${pkgname}-${pkgver}.mmdb" "${pkgdir}/etc/clash/Country.mmdb"
}
