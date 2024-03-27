# Maintainer: Dct Mei <dctxmei@yandex.com>

pkgname=clash-geoip
pkgver=20240327
pkgver() {
  date +'%Y%m%d'
}
pkgrel=1
pkgdesc="GeoIP files for Clash"
arch=(any)
url="https://github.com/MetaCubeX/meta-rules-dat"
license=(CC-BY-SA-4.0 GPL-3.0-or-later)
source=("$url/raw/release/country.mmdb")
sha256sums=('15cd3c51840c1d4849f7933c81e5d35525b5ed980229f6a97af7e4be67126fe7')

package() {
  install -Dm644 country.mmdb "$pkgdir/etc/clash/Country.mmdb"
}
