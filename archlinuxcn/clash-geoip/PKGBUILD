# Maintainer: Dct Mei <dctxmei@yandex.com>

pkgname=clash-geoip
_pkgname=maxmind-geoip
pkgver=20211012
pkgrel=1
pkgdesc="A GeoLite2 data created by MaxMind"
arch=('any')
url="https://github.com/Dreamacro/maxmind-geoip"
license=('custom')
source=("${url}/releases/download/${pkgver}/Country.mmdb")
md5sums=('5efbd72017a294186e9fed4551cf464c')
sha1sums=('baf1f180f9892697b7d3d1b2f2ca1a961912a77c')
sha256sums=('1aa79e4d93b2312bdd6a9251580e48e16d756c6cd159e7275a23f615d46e98ac')

package() {
    install -Dm 644 Country.mmdb -t "${pkgdir}"/etc/clash/
}
