# Maintainer: Dct Mei <dctxmei@yandex.com>

pkgname=clash-geoip
_pkgname=maxmind-geoip
pkgver=20230512
pkgrel=1
pkgdesc="A GeoLite2 data created by MaxMind"
arch=('any')
url="https://github.com/Dreamacro/maxmind-geoip"
license=('custom')
source=("${_pkgname}-${pkgver}.mmdb::${url}/releases/download/${pkgver}/Country.mmdb")
sha256sums=('fd02228be7fba4ecd75e5843415e97187a728c09424bf38e35a95b3d29e602b1')

package() {
    install -Dm0644 "${_pkgname}-${pkgver}.mmdb" "${pkgdir}"/etc/clash/Country.mmdb
}
