# Maintainer: Zenvie <134689569+Zenvie@users.noreply.github.com>
# Contributor: Felix Yan <felixonmars@archlinux.org>

pkgname=v2ray-rules-dat
pkgver=202403262209
pkgrel=1
pkgdesc="Enhanced edition of V2Ray rules dat files"
arch=(any)
url="https://github.com/Loyalsoldier/$pkgname"
license=(CC-BY-SA-4.0 MIT GPL-3.0-or-later)

provides=(v2ray-domain-list-community v2ray-geoip)
conflicts=(v2ray-domain-list-community v2ray-geoip)

source=("$url/releases/download/$pkgver/geoip.dat"
        "$url/releases/download/$pkgver/geosite.dat"
        "$url/releases/download/$pkgver/geoip.dat.sha256sum"
        "$url/releases/download/$pkgver/geosite.dat.sha256sum"
        "https://raw.githubusercontent.com/Loyalsoldier/domain-list-custom/master/LICENSE")
sha256sums=('6e0e73e3656b83f0fad9cb61a8f33b6c896e8cb1cb2db1502f0691640680fe88'
            'a77f367938c4c51c0baffe6d24b7ebd87387b3746dfc186c2ab24ce40d8afb93'
            '52475e5dd7f7d7f4f1dd2adf7bc51550d641a138ebe0aaae53585d4e58c3afbb'
            '48becd46d4f2fbb24a320aa6ff30f0cbc9d782ac19f132222ea1414b48556384'
            '35f18e0331a1ecd1835400c50e3b367c2ce09f6c13d91c4a0f3cb11f71d3bbc3')

prepare() {
  sha256sum -c *.dat.sha256sum
}

package() {  
  install -dm755 "$pkgdir/usr/share/v2ray"
  install -Dm644 *.dat "$pkgdir/usr/share/v2ray"
  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
}
