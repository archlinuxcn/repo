# Maintainer: Dct Mei <dctxmei@yandex.com>

pkgname=clash-geoip
_pkgname=maxmind-geoip
pkgver=20220512
pkgrel=1
pkgdesc="A GeoLite2 data created by MaxMind"
arch=('any')
url="https://github.com/Dreamacro/maxmind-geoip"
license=('custom')
source=("${url}/releases/download/${pkgver}/Country.mmdb")
md5sums=('8810223be9487741232edf439fcedf79')
sha1sums=('7a13b24f74542e1cde1ebbad9a436a22a4ef7070')
sha256sums=('a9f995ac42d64f81bda1d16bbd90c69a860e37f1f787e500597c85d36957104a')

package() {
    install -Dm 644 Country.mmdb -t "${pkgdir}"/etc/clash/
}
