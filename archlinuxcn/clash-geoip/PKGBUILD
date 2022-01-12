# Maintainer: Dct Mei <dctxmei@yandex.com>

pkgname=clash-geoip
_pkgname=maxmind-geoip
pkgver=20220112
pkgrel=1
pkgdesc="A GeoLite2 data created by MaxMind"
arch=('any')
url="https://github.com/Dreamacro/maxmind-geoip"
license=('custom')
source=("${url}/releases/download/${pkgver}/Country.mmdb")
md5sums=('3b9cfa3074eee628f34533552dfb7089')
sha1sums=('724fced669152ceb3cc5d4e1c179083bce09400d')
sha256sums=('79c666f2863a538dd51d9e4f017a37a5a7f17f1640c2dc3bb15f9b4c4280f99a')

package() {
    install -Dm 644 Country.mmdb -t "${pkgdir}"/etc/clash/
}
