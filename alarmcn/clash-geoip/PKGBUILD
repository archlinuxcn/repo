# Maintainer: pngdeity <pngdeity@tutanota.com>
# Contributor: willker <wz dot willker at gmail dot com>
# Contributor: celeste <renzhewudi2013@outlook.com>

_githubname="Loyalsoldier/geoip"

pkgname=clash-geoip
changelog=clash-geoip.changelog
pkgver=202610150028
pkgrel=1
pkgdesc="GeoIP files for Clash"
arch=(any)
url="https://github.com/Loyalsoldier/geoip"
license=(CC-BY-SA-4.0 GPL-3.0-or-later)
source=(
    "${pkgname}-${pkgver}.mmdb::${url}/releases/download/${pkgver}/Country.mmdb"
)
sha256sums=('3530450f4eba9e827bf76934ac2736710590389319e346acb4fc11ce54a19b73')

package() {
    install -Dm0644 "${pkgname}-${pkgver}.mmdb" "${pkgdir}/etc/clash/Country.mmdb"
}
