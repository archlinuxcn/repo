# Maintainer: Zenvie <134689569+Zenvie@users.noreply.github.com>
# Contributor: Felix Yan <felixonmars@archlinux.org>

pkgname=v2ray-rules-dat
pkgver=202405272209
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
sha256sums=('db63f64c77f953d001b5ce7be36b6325fcf3c1bb4a584964709d4d4e183baf77'
            '452dfa76398a9d5dc3a8f02b376a6dacea37053a886eec7e50f01c817370977d'
            '0bae51c69714d6b18483f61ce134be8a5be2fdadb2235835062e639ba68838d0'
            'b29232c15204a7ef8c2c0b79aecafc7d6a3bb6300e47c70cebbe7997721311d9'
            '35f18e0331a1ecd1835400c50e3b367c2ce09f6c13d91c4a0f3cb11f71d3bbc3')

prepare() {
  sha256sum -c *.dat.sha256sum
}

package() {  
  install -dm755 "$pkgdir/usr/share/v2ray"
  install -Dm644 *.dat "$pkgdir/usr/share/v2ray"
  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
}
