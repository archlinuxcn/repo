# Maintainer: Dct Mei <dctxmei@yandex.com>

pkgname=clash-geoip
_pkgname=maxmind-geoip
pkgver=20230312
pkgrel=1
pkgdesc="A GeoLite2 data created by MaxMind"
arch=('any')
url="https://github.com/Dreamacro/maxmind-geoip"
license=('custom')
source=("${_pkgname}-${pkgver}.mmdb::${url}/releases/download/${pkgver}/Country.mmdb")
sha256sums=('63f825cfa1d47e3a31f4c9fe80fcc0f3eb541ea57f2a42089d49f84b26a35221')

package() {
    install -Dm0644 "${_pkgname}-${pkgver}.mmdb" "${pkgdir}"/etc/clash/Country.mmdb
}
