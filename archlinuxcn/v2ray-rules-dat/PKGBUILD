# Maintainer: DeepChirp <DeepChirp@outlook.com>
# Maintainer: hour-keeper <lok-ation@outlook.com>
# Contributor: lilydjwg <lilydjwg@gmail.com>
# Contributor: Zenvie <134689569+Zenvie@users.noreply.github.com>
# Contributor: Felix Yan <felixonmars@archlinux.org>

pkgname=v2ray-rules-dat
pkgver=202512312215
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
sha256sums=('600763effa8d9f029726c3229b7fc5a8ae509e7a4a1381c4a3d643e38cae4459'
            'f86223f9319b4aa92f27f238d08d4aa78760539d263c1c9758cff1205ca7774d')

package() {
    local d
    for d in v2ray xray; do
        install -Dm644 "$srcdir/geoip-$pkgver.dat"   "$pkgdir/usr/share/$d/geoip.dat"
        install -Dm644 "$srcdir/geosite-$pkgver.dat" "$pkgdir/usr/share/$d/geosite.dat"
    done
}
