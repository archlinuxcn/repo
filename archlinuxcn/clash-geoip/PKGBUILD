# Maintainer: Dct Mei <dctxmei@yandex.com>

pkgname=clash-geoip
_pkgname=maxmind-geoip
pkgver=20210612
pkgrel=1
pkgdesc="A GeoLite2 data created by MaxMind"
arch=('any')
url="https://github.com/Dreamacro/maxmind-geoip"
license=('custom')
source=("${url}/releases/download/${pkgver}/Country.mmdb")
md5sums=('023fbc685c2fa9373dfa2746a40048c7')
sha1sums=('2b59ee49aa181aae0753b65bc6631af52b05d774')
sha256sums=('2c59e3eb647abb746cdcd456c815ccdbd7809d0edc58f421418ac45eee41bdd7')

package() {
    install -Dm 644 Country.mmdb -t "${pkgdir}"/etc/clash/
}
