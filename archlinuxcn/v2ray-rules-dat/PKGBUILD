# Maintainer: Zenvie <134689569+Zenvie@users.noreply.github.com>
# Contributor: Chenrry666 <chengruichen3@gmail.com>
# Contributor: Felix Yan <felixonmars@archlinux.org>

pkgname=v2ray-rules-dat
pkgver=None
pkgrel=1
pkgdesc="Enhanced edition of V2Ray rules dat files, compatible with Xray and Hysteria."
arch=(any)
url="https://github.com/Loyalsoldier/$pkgname"
license=(CC-BY-SA-4.0 MIT GPL-3.0-or-later)

provides=(v2ray-domain-list-community v2ray-geoip)
conflicts=(v2ray-domain-list-community v2ray-geoip)

makedepends=(git)

source=("LICENSE::https://raw.githubusercontent.com/Loyalsoldier/domain-list-custom/master/LICENSE")
sha256sums=('35f18e0331a1ecd1835400c50e3b367c2ce09f6c13d91c4a0f3cb11f71d3bbc3')

prepare() {
  git clone --depth 1 --branch release $url release
}

package() {  
  install -dm755 "$pkgdir/usr/share/v2ray"
  install -Dm644 "release/geoip.dat"   "$pkgdir/usr/share/v2ray/geoip.dat"
  install -Dm644 "release/geosite.dat" "$pkgdir/usr/share/v2ray/geosite.dat"

  install -dm755 "$pkgdir/usr/share/xray"
  ln -s "/usr/share/v2ray/geoip.dat" "$pkgdir/usr/share/xray/geoip.dat"
  ln -s "/usr/share/v2ray/geosite.dat" "$pkgdir/usr/share/xray/geosite.dat"

  install -dm755 "$pkgdir/usr/share/hysteria"
  ln -s "/usr/share/v2ray/geoip.dat" "$pkgdir/usr/share/hysteria/geoip.dat"
  ln -s "/usr/share/v2ray/geosite.dat" "$pkgdir/usr/share/hysteria/geosite.dat"

  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
}
