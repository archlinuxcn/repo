# Maintainer: everyx <lunt.luo#gmail.com>

pkgbase=sing-geosite
pkgname=(sing-geosite-db sing-geosite-rule-set)
pkgver=20240823035651
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
sha256sums=('ed604b57bba667098ecbd0f5ecad6b402257b2aede914facd6e533b0991f64d1'
            'a76d2bb567f78d4f194e3bb670bbd65ca9609a570b26fbdcebcd12244cf1843d'
            '3f6a64590cf4364ac3206bb03501ade2967e4790d370412e6bac4fc3dbe697b7'
            'b96e99b7d800a01e3210aeb276f58f2aca42b9a49aace77d80cc7ec3b83a2907'
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
