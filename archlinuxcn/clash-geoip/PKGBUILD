# Maintainer: Dct Mei <dctxmei@yandex.com>

pkgname=clash-geoip
_pkgname=maxmind-geoip
pkgver=20210812
pkgrel=1
pkgdesc="A GeoLite2 data created by MaxMind"
arch=('any')
url="https://github.com/Dreamacro/maxmind-geoip"
license=('custom')
source=("${url}/releases/download/${pkgver}/Country.mmdb")
md5sums=('f901873268f3f71b8f588406f731cf02')
sha1sums=('8ab25a880f913a51b603bccb21190ccf27ae953e')
sha256sums=('6e2265425c3b77d196b4aca6dcd5c22e4ce071bae785f876856a609aec8f73f1')

package() {
    install -Dm 644 Country.mmdb -t "${pkgdir}"/etc/clash/
}
