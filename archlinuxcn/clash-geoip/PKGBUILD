# Maintainer: Dct Mei <dctxmei@yandex.com>

pkgname=clash-geoip
pkgver=20240401
pkgver() {
  date +'%Y%m%d'
}
pkgrel=1
pkgdesc="GeoIP files for Clash"
arch=(any)
url="https://github.com/MetaCubeX/meta-rules-dat"
license=(CC-BY-SA-4.0 GPL-3.0-or-later)
source=("$url/raw/release/country.mmdb")
sha256sums=('4c57de73a8a87129fb0b0c4230e8dfa22a0559e54e096164c4a87974a0ec8675')

package() {
  install -Dm644 country.mmdb "$pkgdir/etc/clash/Country.mmdb"
}
