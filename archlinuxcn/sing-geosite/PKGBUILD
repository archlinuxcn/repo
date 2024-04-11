# Maintainer: everyx <lunt.luo#gmail.com>

pkgbase=sing-geosite
pkgname=(sing-geosite-db sing-geosite-rule-set)
pkgver=20240410101316
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
sha256sums=('7b790836b434e39d67bcbd8e53ba7c00ed359edfc80a52a8e89ce91a21b8c475'
            'd01e4bd7b5b36e91112001703841a7d0a3ca304e4010e73eb2d5e719a335ce95'
            '7c8ab7fb4790d0d754539122b8e590e4c1d2eb055dc8da975b31008f8c19c747'
            '8d14619572fef435d9a9e670b13eaab302318e237a179f992e273b24412bef8c'
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
