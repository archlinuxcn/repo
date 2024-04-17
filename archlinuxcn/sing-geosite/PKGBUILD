# Maintainer: everyx <lunt.luo#gmail.com>

pkgbase=sing-geosite
pkgname=(sing-geosite-db sing-geosite-rule-set)
pkgver=20240416175239
pkgrel=1
pkgdesc="Geosite Database and Rule Set for sing-box"
arch=(any)
url="https://github.com/SagerNet/$pkgbase"
license=(MIT GPL-3.0-or-later)

makedepends=(git)

source=("${pkgver}-geosite.db::$url/releases/download/$pkgver/geosite.db"
        "${pkgver}-geosite.db.sha256sum::$url/releases/download/$pkgver/geosite.db.sha256sum"
        "${pkgver}-geosite-cn.db::$url/releases/download/$pkgver/geosite-cn.db"
        "${pkgver}-geosite-cn.db.sha256sum::$url/releases/download/$pkgver/geosite-cn.db.sha256sum"
        "LICENSE::https://raw.githubusercontent.com/v2fly/domain-list-community/master/LICENSE")
sha256sums=('20d422f751a62feb73191a1e2dc10a46e1bc182f3cacea6586aa012935de5676'
            '60db7760a256106eca981bcf6b923a9da2184a4e578f8e9eda5271840c86ca11'
            'c2b44877b8c2625631be700ba73d12765b2f624e4a8002e3c9d10b9cbd04cd50'
            '8f41b51bf13909b8414b14999aa39f006e47bcc575b153664a7630b7f4c9e404'
            'b9d84a22870d3f21c91a4c6e410c9cc51d00902f5233ad0c84011479244bf7d2')

prepare() {
  mv ${pkgver}-geosite.db geosite.db
  mv ${pkgver}-geosite-cn.db geosite-cn.db
  sha256sum -c ${pkgver}-geosite.db.sha256sum
  sha256sum -c ${pkgver}-geosite-cn.db.sha256sum

  rm -rf rule-set && git clone --depth 1 --branch rule-set $url rule-set
}

package_sing-geosite-db() {
  pkgdesc="sing-geosite (database)"
  provides=($pkgbase)

  install -dm755 "$pkgdir/usr/share/sing-box"
  install -Dm644 geosite.db "$pkgdir/usr/share/sing-box"
  install -Dm644 geosite-cn.db "$pkgdir/usr/share/sing-box"
  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
}

package_sing-geosite-rule-set() {
  pkgdesc="sing-geosite (rule-set)"
  provides=($pkgbase)

  install -dm755 "$pkgdir/usr/share/sing-box/$pkgname"
  install -Dm644 rule-set/geosite-*.srs "$pkgdir/usr/share/sing-box/$pkgname"
  install -Dm644 LICENSE -t "$pkgdir/usr/share/licenses/$pkgname"
}
