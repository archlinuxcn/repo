# Maintainer: everyx <lunt.luo#gmail.com>

pkgbase=sing-geoip
pkgname=(sing-geoip-db sing-geoip-rule-set)
pkgver=20241112
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
sha256sums=('c801efffb30e5b172f6579872252b6f56638e7caf3cf95e1fb5468ee04229380'
            'bdc4f7297c04881f9ce9e0e0d845666304a4a40838f82bc0d03622f302e973b0'
            '29e7a6943f95ec4eb9fe17ca7f2c69fa1bd7d49b00d154d2487cfd2932dca7b3'
            'b4ffaa53f45084a75ce582f852bd3739a04a1f7dc8ccfd0811795ecbe537c812'
            'd7d87b9b2f9b96f242e534585e66b897c2957b95b49a4699ef4a04b736d0d4d1')

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
