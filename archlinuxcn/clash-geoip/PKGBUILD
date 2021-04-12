# Maintainer: Dct Mei <dctxmei@yandex.com>

pkgname=clash-geoip
_pkgname=maxmind-geoip
pkgver=20210412
pkgrel=1
pkgdesc="A GeoLite2 data created by MaxMind"
arch=('any')
url="https://github.com/Dreamacro/maxmind-geoip"
license=('custom')
source=("${url}/releases/download/${pkgver}/Country.mmdb")
md5sums=('4b3bdf60180d83508667cc0c9420970c')
sha1sums=('bf0ab59d155c903c1f902bcf2d4e9811da93201e')
sha256sums=('21332b83dde95ed408b458cad66b9b4e5605bcc0d6c1be23c08b0f09c2c7e59b')

package() {
    install -Dm 644 Country.mmdb -t "${pkgdir}"/etc/clash/
}
