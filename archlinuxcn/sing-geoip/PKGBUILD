# Maintainer: everyx <lunt.luo#gmail.com>

pkgbase=sing-geoip
pkgname=(sing-geoip-rule-set sing-geoip-db)
pkgver=20240312
pkgrel=3
pkgdesc="GeoIP Database and Rule Set for sing-box"
arch=(any)
url="https://github.com/SagerNet/$pkgbase"
license=(CC-BY-SA-4.0 GPL-3.0-or-later)

makedepends=(git)

source=("geoip.db::$url/releases/download/$pkgver/geoip.db")
sha256sums=('77879a4239ed28a9835e7db1d7f55dd3f9540904714125cb39cc3425e61b7fd4')

prepare() {
  git clone --depth 1 --branch rule-set $url
}

package_sing-geoip-rule-set() {
  pkgdesc="sing-geoip (rule-set)"
  provides=($pkgbase)

  install -dm755 "$pkgdir/usr/share/sing-box/$pkgname"
  install -Dm644 $pkgbase/*.srs "$pkgdir/usr/share/sing-box/$pkgname"
}

package_sing-geoip-db() {
  pkgdesc="sing-geoip (database)"
  provides=($pkgbase)

  install -dm755 "$pkgdir/usr/share/sing-box"
  install -Dm644 geoip.db "$pkgdir/usr/share/sing-box"
}
