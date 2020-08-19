# Maintainer: Dct Mei <dctxmei@gmail.com>

pkgname=golang-clash-geoip
_pkgname=maxmind-geoip
pkgver=20200812
pkgrel=1
pkgdesc="A GeoLite2 data created by MaxMind"
arch=('any')
url="https://github.com/Dreamacro/maxmind-geoip"
license=('custom')
source=("${url}/releases/download/${pkgver}/Country.mmdb")
md5sums=('09a90b1a1dd36ffdcfdd21fac4ab4c2f')
sha1sums=('86bd25e7c30b1f67115421acd3e32f7522a33877')
sha256sums=('b0868bd0e4f9885d607befb31167fe5723d7579acb842862fd2fd04ec547b406')

package() {
    install -Dm 755 Country.mmdb -t "${pkgdir}"/etc/clash/
}
