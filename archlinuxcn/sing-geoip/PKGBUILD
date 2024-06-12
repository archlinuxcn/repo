# Maintainer: everyx <lunt.luo#gmail.com>

pkgbase=sing-geoip
pkgname=(sing-geoip-db sing-geoip-rule-set)
pkgver=20240612
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
sha256sums=('71437ad27893bd660020173f376faa5ac890fdc890a60b13c0478676bb31e962'
            '9e6b1241001c15701e19106c3695c7f0b143bffc13d442564c7d218838c76c3b'
            '92a6f06d446fac776ca7af1343e4ecb5ab51b5ca0912a8f49c223a00c1a9e845'
            '85655a0dadc531a30d236ea4eb30e2144f8ff709beb9bdb6c56bf3f5ee883fd5')

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
