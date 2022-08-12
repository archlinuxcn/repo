# Maintainer: Dct Mei <dctxmei@yandex.com>

pkgname=clash-geoip
_pkgname=maxmind-geoip
pkgver=20220812
pkgrel=1
pkgdesc="A GeoLite2 data created by MaxMind"
arch=('any')
url="https://github.com/Dreamacro/maxmind-geoip"
license=('custom')
source=("${url}/releases/download/${pkgver}/Country.mmdb")
md5sums=('7b2c7084ad1b71146948d62d60e3cacd')
sha1sums=('b540bca1bcb46a37b1879893f3f82fc83aa7905c')
sha256sums=('532a0c07ea092cfd25e4678ba4cb31e728e34634cc334582d65a245c6d85ab75')

package() {
    install -Dm 644 Country.mmdb -t "${pkgdir}"/etc/clash/
}
