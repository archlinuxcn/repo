# Maintainer: everyx <lunt.luo#gmail.com>

pkgbase=sing-geosite
pkgname=(sing-geosite-db sing-geosite-rule-set)
pkgver=20240612095513
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
sha256sums=('ef3b80d6eaca118ede263ee71718e9455237b7463c0dbcbd27dc47f35d31cd87'
            'e60172651e9fc96954e0438553bb3f574f4d94f911e5f91521ae2d7c4d8380f9'
            'd947d629c703ccefe25ab2c4d60ef26959fc1f5e6b6caca2072aafddbb123e0e'
            '0a2a3064c234283bd6a098c8fcb234e4228ce83cf4e290682212e56bc81b0a58'
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
