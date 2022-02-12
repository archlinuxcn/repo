# Maintainer: Dct Mei <dctxmei@yandex.com>

pkgname=clash-geoip
_pkgname=maxmind-geoip
pkgver=20220212
pkgrel=1
pkgdesc="A GeoLite2 data created by MaxMind"
arch=('any')
url="https://github.com/Dreamacro/maxmind-geoip"
license=('custom')
source=("${url}/releases/download/${pkgver}/Country.mmdb")
md5sums=('9f48036dea32314763c89bec62f0600c')
sha1sums=('e04ca6190311ab8dc86056b7b5fa6405e502015f')
sha256sums=('d430e181781764c10c1ce6db2c1cc893e2ffe8883053ba059ad8e1818b738759')

package() {
    install -Dm 644 Country.mmdb -t "${pkgdir}"/etc/clash/
}
