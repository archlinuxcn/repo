# Maintainer: everyx <lunt.luo#gmail.com>

pkgbase=sing-geoip
pkgname=(sing-geoip-db sing-geoip-rule-set)
pkgver=20250512
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
sha256sums=('246afa696e79c9f4087de20ec3cae323ed87f1b87cbd88fe8b4f99dd5e872cba'
            '7c669d2037fc21669daebe2ef98e0199a4e5c75866a374ceb6ed1094de266d4b'
            '9746ded8a3cae866884f5b6f140eab574786c0c66e4a144e6b540b40296adabb'
            '01b8a836e8f9d270a6ed0aadf8f90246be8ce748ae5963cc4d79b0d52733b8da'
            'f7ed4df351153b8e2734f5c0ea16173b911b721506892182d68b07526e2d3dac')

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
