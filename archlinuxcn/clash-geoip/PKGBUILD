# Maintainer: Dct Mei <dctxmei@yandex.com>

pkgname=clash-geoip
_pkgname=maxmind-geoip
pkgver=20220912
pkgrel=2
pkgdesc="A GeoLite2 data created by MaxMind"
arch=('any')
url="https://github.com/Dreamacro/maxmind-geoip"
license=('custom')
source=("${url}/releases/download/${pkgver}/Country.mmdb")
sha256sums=('608423b966e2ce178413d9202fe8414b518019fd8f6e9696e66bbf9629bd43d0')

package() {
    install -Dm0644 Country.mmdb -t "${pkgdir}"/etc/clash/
}
