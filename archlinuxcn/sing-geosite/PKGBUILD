# Maintainer: everyx <lunt.luo#gmail.com>

pkgbase=sing-geosite
pkgname=(sing-geosite-db sing-geosite-rule-set)
pkgver=20250521095120
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
sha256sums=('48e4f4c93d09691ff99ef9d5540a081244430df830fca72b7e3efa1691081eed'
            'b003e0c132f4b0a23c6e6db62e7ba58127bd1eb1be5b8fc30839a1cfbe51c0b4'
            'cc0dec48377130b137bb2eee436d1d7c9ca2f77031b8483d92cf62ca6d3db884'
            'da1a2039867835ac3c4f86dbfa844e5ebfd30e11bae8aa1de3966ba80223f036'
            '296c0393c080b06c84666171cca09cc2955c3a58765b4bd24f0dbcbdc951d1b4'
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
