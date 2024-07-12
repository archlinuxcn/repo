# Maintainer: everyx <lunt.luo#gmail.com>

pkgbase=sing-geoip
pkgname=(sing-geoip-db sing-geoip-rule-set)
pkgver=20240712
pkgrel=1
pkgdesc="GeoIP Database and Rule Set for sing-box"
arch=(any)
url="https://github.com/SagerNet/$pkgbase"
license=(CC-BY-SA-4.0 GPL-3.0-or-later)

makedepends=(git)

source=("${pkgver}-geoip.db::$url/releases/download/$pkgver/geoip.db"
        "${pkgver}-geoip.db.sha256sum::$url/releases/download/$pkgver/geoip.db.sha256sum"
        "${pkgver}-geoip-cn.db::$url/releases/download/$pkgver/geoip-cn.db"
        "${pkgver}-geoip-cn.db.sha256sum::$url/releases/download/$pkgver/geoip-cn.db.sha256sum")
sha256sums=('8f1f8bd8eaec92e33f9b785aeb37835b11603e2aff15c8f93ffd6f69928b5ada'
            'ebe9fae32c61e053f4b86b322c60a33c1b4ecf4d55d6372cfb4b30e7aa9f0e49'
            'ff9861710ca825492b5529f90fd3618ff5098c5c7880915f2552a129cabce513'
            '5150f11496a6e84b0a5917eec2d2e14711965059cf864d98e5913b299765ea32')

prepare() {
  mv ${pkgver}-geoip.db geoip.db
  mv ${pkgver}-geoip-cn.db geoip-cn.db
  sha256sum -c ${pkgver}-geoip.db.sha256sum
  sha256sum -c ${pkgver}-geoip-cn.db.sha256sum

  rm -rf rule-set && git clone --depth 1 --branch rule-set $url rule-set
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
