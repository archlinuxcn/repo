# Maintainer: everyx <lunt.luo#gmail.com>

pkgbase=sing-geoip
pkgname=(sing-geoip-db sing-geoip-rule-set)
pkgver=20260112
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
sha256sums=('7b6348b4dad36a6b0c62f06f8f69cb00b2f438ee96dbae739f49d0ac387ad42a'
            'a00de5b4a6374efce7f47fd2e32fc9671d46e7c337d4351971c363b32d34f9b6'
            'c73194ee7afd793e869995e2d5421bd335c47ec4fb9a87e56da74d9e6c2eb216'
            '338bd3498a82958f40ef257325de1b7211e3c2cd0e9d8233c00821750f4eddb9'
            '5bf453275426082a9eabd9a32b575b669416336c5003e5a4d919fe08af6192dd')

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
