# Maintainer: DeepChirp <deepchirp@archlinuxcn.org>
# Maintainer: hour-keeper <lok-ation@outlook.com>
# Contributor: lilydjwg <lilydjwg@gmail.com>
# Contributor: Zenvie <134689569+Zenvie@users.noreply.github.com>
# Contributor: Felix Yan <felixonmars@archlinux.org>

pkgname=v2ray-rules-dat
pkgver=202609012343
pkgrel=1
pkgdesc="Enhanced edition of V2Ray rules dat files."
arch=('any')
_author=Loyalsoldier
url="https://github.com/${_author}/${pkgname}"
license=('GPL3')
provides=('v2ray-domain-list-community' 'v2ray-geoip' 'xray-geoip' 'xray-geosite')
conflicts=('v2ray-domain-list-community' 'v2ray-geoip' 'xray-geoip' 'xray-geosite')
source=("geoip-$pkgver.dat::${url}/releases/download/${pkgver}/geoip.dat"
        "geosite-$pkgver.dat::${url}/releases/download/${pkgver}/geosite.dat")
sha256sums=('0d5d2ba0c5a5c58027fd1347a6afd57c9470799b6bb3cbc274fd4657ed8de382'
            '81f0437edc89f76df985904c24468304b2fdc51249a759f54758b019a3d918b4')

package() {
    local d
    for d in v2ray xray; do
        install -Dm644 "$srcdir/geoip-$pkgver.dat"   "$pkgdir/usr/share/$d/geoip.dat"
        install -Dm644 "$srcdir/geosite-$pkgver.dat" "$pkgdir/usr/share/$d/geosite.dat"
    done
}
