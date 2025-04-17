# Maintainer: everyx <lunt.luo#gmail.com>

pkgbase=sing-geosite
pkgname=(sing-geosite-db sing-geosite-rule-set)
pkgver=20250416191447
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
sha256sums=('81638a9bf9a2062a8b3f3ff341a1bfb71ad341e27ce2bfbf1b790e41dfd20d44'
            '309d01ab157621cdf16e013ad6afcb62a88998172a9544434732fbb437e89d7b'
            '3fd5773ba8213fa12eec045fa9fb68c6fd2dc36c1d478250c275100d5fd8eb5c'
            '08e84e7689ce2c3d43154be3b1459b57611c0e5d40e462581ce9c840c454926f'
            'cb8831a70d75e5db010411fdfa69bc100e602be691702929224b48f52111cd33'
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
