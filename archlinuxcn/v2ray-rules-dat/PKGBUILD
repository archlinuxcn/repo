# Maintainer: DeepChirp <DeepChirp@outlook.com>
# Maintainer: hour-keeper <lok-ation@outlook.com>
# Contributor: lilydjwg <lilydjwg@gmail.com>
# Contributor: Zenvie <134689569+Zenvie@users.noreply.github.com>
# Contributor: Felix Yan <felixonmars@archlinux.org>

pkgname=v2ray-rules-dat
pkgver=202602082220
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
sha256sums=('8cf3dac7d99e428a380bd3aa1330f57718a794d45fe4f9dd20077c010dc0bcdb'
            '4c744d23b978c7c668be9f78ae618bcf331a52c75babe83eaa8590b5f109f288')

package() {
    local d
    for d in v2ray xray; do
        install -Dm644 "$srcdir/geoip-$pkgver.dat"   "$pkgdir/usr/share/$d/geoip.dat"
        install -Dm644 "$srcdir/geosite-$pkgver.dat" "$pkgdir/usr/share/$d/geosite.dat"
    done
}
