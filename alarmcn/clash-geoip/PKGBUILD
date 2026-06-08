# Maintainer: pngdeity <pngdeity@tutanota.com>
# Contributor: willker <wz dot willker at gmail dot com>
# Contributor: celeste <renzhewudi2013@outlook.com>

_githubname="Loyalsoldier/geoip"

pkgname=clash-geoip
pkgver=202605210051
pkgrel=1
pkgdesc="GeoIP files for Clash"
arch=(any)
url="https://github.com/Loyalsoldier/geoip"
license=(CC-BY-SA-4.0 GPL-3.0-or-later)
source=(
    "${pkgname}-${pkgver}.mmdb::${url}/releases/download/${pkgver}/Country.mmdb"
)
sha256sums=('12bb95152b349818de5d5166d9866e99dcc9979fafc74add7a86a6325bda4d32')

package() {
    install -Dm0644 "${pkgname}-${pkgver}.mmdb" "${pkgdir}/etc/clash/Country.mmdb"
}
