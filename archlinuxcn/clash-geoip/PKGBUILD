# Maintainer: Dct Mei <dctxmei@yandex.com>

pkgname=clash-geoip
_pkgname=maxmind-geoip
pkgver=20220612
pkgrel=1
pkgdesc="A GeoLite2 data created by MaxMind"
arch=('any')
url="https://github.com/Dreamacro/maxmind-geoip"
license=('custom')
source=("${url}/releases/download/${pkgver}/Country.mmdb")
md5sums=('666dd848df2122e19f55f678c569445a')
sha1sums=('3466737e7589b2ad459ecda975eccac4ac888336')
sha256sums=('f4b0ce73b4a49a785bba8dfb031da86360d62e3999e409869c8db821fd14d213')

package() {
    install -Dm 644 Country.mmdb -t "${pkgdir}"/etc/clash/
}
