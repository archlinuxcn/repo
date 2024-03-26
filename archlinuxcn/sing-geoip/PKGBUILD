# Maintainer: everyx <lunt.luo#gmail.com>

pkgbase=sing-geoip
pkgname=(sing-geoip-db sing-geoip-rule-set)
pkgver=20240312
pkgrel=6
pkgdesc="GeoIP Database and Rule Set for sing-box"
arch=(any)
url="https://github.com/SagerNet/$pkgbase"
license=(CC-BY-SA-4.0 GPL-3.0-or-later)

makedepends=(git)

source=("$url/releases/download/$pkgver/geoip.db"
        "$url/releases/download/$pkgver/geoip.db.sha256sum")
sha256sums=('77879a4239ed28a9835e7db1d7f55dd3f9540904714125cb39cc3425e61b7fd4'
            'f150da7d973e20ccae298569ae261d2f34936414bdca45fad87e4e3b9ce09b71')

prepare() {
  sha256sum -c geoip.db.sha256sum

  mkdir rule-set
  git clone --depth 1 --branch rule-set $url rule-set
}

package_sing-geoip-db() {
  pkgdesc="sing-geoip (database)"
  provides=($pkgbase)

  install -dm755 "$pkgdir/usr/share/sing-box"
  install -Dm644 geoip.db "$pkgdir/usr/share/sing-box"
}

package_sing-geoip-rule-set() {
  pkgdesc="sing-geoip (rule-set)"
  provides=($pkgbase)

  install -dm755 "$pkgdir/usr/share/sing-box/$pkgname"
  install -Dm644 rule-set/geoip-*.srs "$pkgdir/usr/share/sing-box/$pkgname"
}
