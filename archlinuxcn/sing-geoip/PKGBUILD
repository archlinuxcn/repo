# Maintainer: everyx <lunt.luo#gmail.com>

pkgbase=sing-geoip
pkgname=(sing-geoip-db sing-geoip-rule-set)
pkgver=20240412
pkgrel=1
pkgdesc="GeoIP Database and Rule Set for sing-box"
arch=(any)
url="https://github.com/SagerNet/$pkgbase"
license=(CC-BY-SA-4.0 GPL-3.0-or-later)

makedepends=(git)

source=("${pkgver}-geoip.db::$url/releases/download/$pkgver/geoip.db"
        "${pkgver}-geoip.db.sha256sum::$url/releases/download/$pkgver/geoip.db.sha256sum"
        "${pkgver}-geoip-cn.db::$url/releases/download/$pkgver/geoip-cn.db"
        "${pkgver}-geoip-cn.db.sha256sum::$url/releases/download/$pkgver/geoip-cn.db.sha256sum")
sha256sums=('024c9e476bb6cf4b56efdf64883ae825c572be0b12d7764e1c77853999ee9a66'
            '87dcfb8b5a0fa85570a513b0b7561b267ad13c92e36056d2b4ea65cd8267b7a8'
            'd31489d770229d483417e7860b0f3ad7bc77b1fa3e5722f7b993197ecb2143c6'
            'eb0db456af12209cc0f3b61759c59d5ca807e2da59746fdbad8072aa7147e5cc')

prepare() {
  mv ${pkgver}-geoip.db geoip.db
  mv ${pkgver}-geoip-cn.db geoip-cn.db
  sha256sum -c ${pkgver}-geoip.db.sha256sum
  sha256sum -c ${pkgver}-geoip-cn.db.sha256sum

  rm -rf rule-set && git clone --depth 1 --branch rule-set $url rule-set
}

package_sing-geoip-db() {
  pkgdesc="sing-geoip (database)"
  provides=($pkgbase)

  install -dm755 "$pkgdir/usr/share/sing-box"
  install -Dm644 geoip.db "$pkgdir/usr/share/sing-box"
}

package_sing-geoip-rule-set() {
  pkgdesc="sing-geoip (rule-set)"
  provides=($pkgbase)

  install -dm755 "$pkgdir/usr/share/sing-box/$pkgname"
  install -Dm644 rule-set/geoip-*.srs "$pkgdir/usr/share/sing-box/$pkgname"
}
