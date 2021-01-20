# Maintainer: Dct Mei <dctxmei@gmail.com>

pkgname=clash-geoip
_pkgname=maxmind-geoip
pkgver=20210112
pkgrel=1
pkgdesc="A GeoLite2 data created by MaxMind"
arch=('any')
url="https://github.com/Dreamacro/maxmind-geoip"
license=('custom')
source=("${url}/releases/download/${pkgver}/Country.mmdb")
md5sums=('9b0215597657cb409dadbccf3a1891b1')
sha1sums=('ab8beee91ac8e4bce7a2872fb300cceb4de2325e')
sha256sums=('823ddedeff08a1589f580148bb76ed486f4e299a076f5c8066650c34ab6a88ac')

package() {
    install -Dm 644 Country.mmdb -t "${pkgdir}"/etc/clash/
}
