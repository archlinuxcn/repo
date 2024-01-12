# Maintainer: Dct Mei <dctxmei@yandex.com>

pkgname=clash-geoip
_pkgname=maxmind-geoip
pkgver=20240112
pkgrel=1
pkgdesc="A GeoLite2 data created by MaxMind"
arch=('any')
url="https://github.com/Dreamacro/maxmind-geoip"
license=('custom')
source=("${_pkgname}-${pkgver}.mmdb::${url}/releases/download/${pkgver}/Country.mmdb")
sha256sums=('46744f18c1dbfa07222b1555d03a0afc4ffbb08ed96fdcafb6a1d8b580c2d794')

package() {
    install -Dm0644 "${_pkgname}-${pkgver}.mmdb" "${pkgdir}"/etc/clash/Country.mmdb
}
