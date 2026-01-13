# Maintainer: everyx <lunt.luo#gmail.com>

pkgbase=sing-geosite
pkgname=(sing-geosite-db sing-geosite-rule-set)
pkgver=20260112053243
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
sha256sums=('9569a4b802cc6f1de2c3a06c2e9e8b071469c0f27a3e234056236fc74cffe531'
            '6a9f2f3a437028c124d776df5f99832b743d6e98c29c4dd8445935d08f1f9e48'
            '874dceeb53c638b6495f2aefe19f9e8d95d31f1b795d219af4eadd5850a150bd'
            '2f57c6bb480659d559374cc6c5591844120528d56cab003d5d4a190e1e4e1c7a'
            '47bac136a88ec9e20a9df8dc8a59401e04caa939183bb42174c227e9bb10ce75'
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
