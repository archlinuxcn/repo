# Maintainer: everyx <lunt.luo#gmail.com>

pkgbase=sing-geoip
pkgname=(sing-geoip-db sing-geoip-rule-set)
pkgver=20250912
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
sha256sums=('a8018d5672b9a29136207c7048534d8f5d122fa8244eb129810c493a93b524b4'
            'b2513f4fec2d6c37a14cd897d6ca14c32634a32d1104e94ebf89c947d8e43af2'
            'b32d8adba16e4e09e42122bb4822e03f146488aa186c54f374582b63a984e493'
            'ec72724ca377a343011709c6bb11ad967db2ac5ae6163d31061394a0c856aeda'
            '96f046274d130d21ec93df7f87c8ebe80bca94c7c164c38f52c373806220a03b')

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
