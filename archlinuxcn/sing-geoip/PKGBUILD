# Maintainer: everyx <lunt.luo#gmail.com>

pkgbase=sing-geoip
pkgname=(sing-geoip-db sing-geoip-rule-set)
pkgver=20241012
pkgrel=1
pkgdesc="GeoIP Database and Rule Sets for sing-box"
arch=(any)
url="https://github.com/SagerNet/$pkgbase"
license=(CC-BY-SA-4.0 GPL-3.0-or-later)

source=("${pkgver}-geoip.db::$url/releases/download/$pkgver/geoip.db"
        "${pkgver}-geoip.db.sha256sum::$url/releases/download/$pkgver/geoip.db.sha256sum"
        "${pkgver}-geoip-cn.db::$url/releases/download/$pkgver/geoip-cn.db"
        "${pkgver}-geoip-cn.db.sha256sum::$url/releases/download/$pkgver/geoip-cn.db.sha256sum"
        "${pkgver}-rule-set.tar.gz::$url/archive/refs/heads/rule-set.tar.gz")
sha256sums=('fdbdf516e073feeb5eda11ce5af70e2337cc2bc864f047be703c0eaa58d89196'
            'f10dd4e7aba665a0dace6197c9821f18681ee3fdbdb160b3954491b16a331a11'
            '9e15e1ad32fe9f9e8bf895b49bf17a479a1d7dcecb72c1931cd783dd80d5ed3b'
            '3b924f3defb63d0aec2360f17bef7826405945c75044d80de47699e32cb58bc6'
            '020c27381ff70ded69691a7b3c30abe1d5fc80e66717792ceec3348e2c375fc3')

prepare() {
  mv ${pkgver}-geoip.db geoip.db
  mv ${pkgver}-geoip-cn.db geoip-cn.db
  sha256sum -c ${pkgver}-geoip.db.sha256sum
  sha256sum -c ${pkgver}-geoip-cn.db.sha256sum
}

package_sing-geoip-db() {
  pkgdesc="GeoIP Database for sing-box"
  provides=($pkgbase)

  install -dm755 "$pkgdir/usr/share/sing-box"
  install -Dm644 geoip*.db "$pkgdir/usr/share/sing-box"
}

package_sing-geoip-rule-set() {
  pkgdesc="GeoIP Rule Sets for sing-box"
  provides=($pkgbase)

  install -dm755 "$pkgdir/usr/share/sing-box/rule-set"
  install -Dm644 ${pkgbase}-rule-set/geoip-*.srs "$pkgdir/usr/share/sing-box/rule-set"

  install -dm755 "$pkgdir/usr/share/sing-box/$pkgname"
  for _file in "$pkgdir"/usr/share/sing-box/rule-set/*; do
    _rule_set=$(basename "$_file")
    ln -s "/usr/share/sing-box/rule-set/$_rule_set" "$pkgdir/usr/share/sing-box/$pkgname/"
  done
}
