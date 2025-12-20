# Maintainer: everyx <lunt.luo#gmail.com>

pkgbase=sing-geosite
pkgname=(sing-geosite-db sing-geosite-rule-set)
pkgver=20251219140209
pkgrel=1
pkgdesc="Geosite Database and Rule Sets for sing-box"
arch=(any)
url="https://github.com/SagerNet/$pkgbase"
license=(MIT GPL-3.0-or-later)

source=("${pkgver}-geosite.db::$url/releases/download/$pkgver/geosite.db"
        "${pkgver}-geosite.db.sha256sum::$url/releases/download/$pkgver/geosite.db.sha256sum"
        "${pkgver}-geosite-cn.db::$url/releases/download/$pkgver/geosite-cn.db"
        "${pkgver}-geosite-cn.db.sha256sum::$url/releases/download/$pkgver/geosite-cn.db.sha256sum"
        "${pkgver}-rule-set.tar.gz::$url/archive/refs/heads/rule-set.tar.gz"
        "${pkgver}-LICENSE::https://raw.githubusercontent.com/v2fly/domain-list-community/master/LICENSE")
sha256sums=('8d1fa03f22ef4ed2b70244f01ac3e9eaa36e8cd60bcbeb5cc27dca4d0e1b7dd8'
            '1c26a2272277c6d39eb6e1c0b1abc1bb47b17d3b04dacb8d9ca9ce0cd88eee79'
            'a169e3434e9829678970136566457c51f80f072967453670e72f299bff428eb3'
            '66691704e272a1a702093993c50de05da75429f3cf9dcc701a90c4527a244eb8'
            'f5854db7707b58021775da41122b28bd751220a1e5945ebcb0b761b8e6ac566c'
            'b9d84a22870d3f21c91a4c6e410c9cc51d00902f5233ad0c84011479244bf7d2')

prepare() {
  mv ${pkgver}-geosite.db geosite.db
  mv ${pkgver}-geosite-cn.db geosite-cn.db
  sha256sum -c ${pkgver}-geosite.db.sha256sum
  sha256sum -c ${pkgver}-geosite-cn.db.sha256sum
}

package_sing-geosite-db() {
  pkgdesc="Geosite Database for sing-box"
  provides=($pkgbase)

  install -Dm644 ${pkgver}-LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
  install -dm755 "$pkgdir/usr/share/sing-box"
  install -Dm644 geosite*.db "$pkgdir/usr/share/sing-box"
}

package_sing-geosite-rule-set() {
  pkgdesc="Geosite Rule Sets for sing-box"
  provides=($pkgbase)

  install -Dm644 ${pkgver}-LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"

  install -dm755 "$pkgdir/usr/share/sing-box/rule-set"
  install -Dm644 $pkgbase-rule-set/*.srs "$pkgdir/usr/share/sing-box/rule-set"

  install -dm755 "$pkgdir/usr/share/sing-box/$pkgname"
  for _file in "$pkgdir"/usr/share/sing-box/rule-set/*; do
    _rule_set=$(basename "$_file")
    ln -s "/usr/share/sing-box/rule-set/$_rule_set" "$pkgdir/usr/share/sing-box/$pkgname/"
  done
}
