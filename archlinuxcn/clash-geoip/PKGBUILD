# Maintainer: Dct Mei <dctxmei@yandex.com>

pkgname=clash-geoip
_pkgname=maxmind-geoip
pkgver=20221112
pkgrel=1
pkgdesc="A GeoLite2 data created by MaxMind"
arch=('any')
url="https://github.com/Dreamacro/maxmind-geoip"
license=('custom')
source=("${url}/releases/download/${pkgver}/Country.mmdb")
sha256sums=('b22fd1cc9bd76c0706ed6cafefcd07c2bfb5a22581faebdcd9161b9d8a44d0c0')

package() {
    install -Dm0644 Country.mmdb -t "${pkgdir}"/etc/clash/
}
