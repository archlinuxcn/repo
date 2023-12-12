# Maintainer: Dct Mei <dctxmei@yandex.com>

pkgname=clash-geoip
_pkgname=maxmind-geoip
pkgver=20231212
pkgrel=1
pkgdesc="A GeoLite2 data created by MaxMind"
arch=('any')
url="https://github.com/Dreamacro/maxmind-geoip"
license=('custom')
source=("${_pkgname}-${pkgver}.mmdb::${url}/releases/download/${pkgver}/Country.mmdb")
sha256sums=('87a1288df3967c3c03e4092f6fc36b4af837c7241984e52b2a1531956c22a3c0')

package() {
    install -Dm0644 "${_pkgname}-${pkgver}.mmdb" "${pkgdir}"/etc/clash/Country.mmdb
}
