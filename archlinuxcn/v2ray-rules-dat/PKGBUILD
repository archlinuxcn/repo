# Maintainer: Zenvie <134689569+Zenvie@users.noreply.github.com>
# Contributor: Felix Yan <felixonmars@archlinux.org>

pkgname=v2ray-rules-dat
pkgver=202403282209
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
sha256sums=('d12392c1f4b379eed4c4969adc71e0a3a714a2e4731b050ad7bb7d5e4f822d6c'
            '3437005769efe42a7349cd598da53647cb9640066b9b1b4f8bba83ac81161787'
            '5beee3947b5fe4b8800ccd56f4b579642635c20596711b89975da5a3da25b907'
            '1cfa4b315a9dfa10b8ce234819a2e32c20e04f2a55a4cc24e5b208a8e57d5564'
            '35f18e0331a1ecd1835400c50e3b367c2ce09f6c13d91c4a0f3cb11f71d3bbc3')

prepare() {
  sha256sum -c *.dat.sha256sum
}

package() {  
  install -dm755 "$pkgdir/usr/share/v2ray"
  install -Dm644 *.dat "$pkgdir/usr/share/v2ray"
  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
}
