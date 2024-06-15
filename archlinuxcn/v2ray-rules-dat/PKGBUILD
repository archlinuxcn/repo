# Maintainer: Zenvie <134689569+Zenvie@users.noreply.github.com>
# Contributor: Felix Yan <felixonmars@archlinux.org>

pkgname=v2ray-rules-dat
pkgver=202406142211
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
sha256sums=('20c29c916b8fdeb9d1b2d39ee842aa955ae2559feca07d108c1f521d88521ebe'
            '6b3c9c764a48296ad0d601df512da266355db588fa0c53623de2bde7a96e7521'
            '1f760aa54284d75637714882c62a303264e8c8c5d2f0e3300b9969f59dd54e7c'
            '30d46c107643ce0cecbb6f46713be9616852e1df071fd0095249903e270102b9'
            '35f18e0331a1ecd1835400c50e3b367c2ce09f6c13d91c4a0f3cb11f71d3bbc3')

prepare() {
  sha256sum -c *.dat.sha256sum
}

package() {  
  install -dm755 "$pkgdir/usr/share/v2ray"
  install -Dm644 *.dat "$pkgdir/usr/share/v2ray"
  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
}
