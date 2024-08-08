# Maintainer: Dct Mei <dctxmei@yandex.com>

pkgname=clash-geoip
pkgver=202408080106
pkgrel=1
pkgdesc="GeoIP files for Clash"
arch=(any)
url="https://github.com/Loyalsoldier/geoip"
license=(CC-BY-SA-4.0 GPL-3.0-or-later)
source=("${pkgname}-${pkgver}.mmdb::${url}/releases/download/${pkgver}/Country.mmdb")
sha256sums=('c942c3de241e7bc115f6b73831153cba18e0faec42d86a9a1f0fd89780d91c80')

package() {
    install -Dm0644 "${pkgname}-${pkgver}.mmdb" "${pkgdir}/etc/clash/Country.mmdb"
}
