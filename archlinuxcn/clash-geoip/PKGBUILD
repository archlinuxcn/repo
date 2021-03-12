# Maintainer: Dct Mei <dctxmei@yandex.com>

pkgname=clash-geoip
_pkgname=maxmind-geoip
pkgver=20210312
pkgrel=1
pkgdesc="A GeoLite2 data created by MaxMind"
arch=('any')
url="https://github.com/Dreamacro/maxmind-geoip"
license=('custom')
source=("${url}/releases/download/${pkgver}/Country.mmdb")
md5sums=('7ad42475f306657c29aa276144e26bbf')
sha1sums=('428250c0e54e8ef1fb2da35ef3e8187a6ef95ae5')
sha256sums=('73c1a970504bf27390efc3fd4bdb8f45d1a433da5aef4df7debe2982dbccdeab')

package() {
    install -Dm 644 Country.mmdb -t "${pkgdir}"/etc/clash/
}
