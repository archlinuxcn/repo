# Maintainer: everyx <lunt.luo#gmail.com>

pkgbase=sing-geosite
pkgname=(sing-geosite-db sing-geosite-rule-set)
pkgver=20240920063125
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
sha256sums=('34774e4bb1865f8a4a2696400d8211e4ad4dc3deb0d78b50a2dc70f5338a74f3'
            'e2986fdf7cf78061a437afeadb7128c60f033a8c0bd963f66062d986f0b849b9'
            '5336b6e50d0f53e7f2caa35332462603a4c6f980f85979e864fdf68983082873'
            'ba5a19d0e5a96564d40d26423cc9b235ccbb401ce90298bfbcd60e928b2f74f3'
            '96f1a4fa79655b7627f43b909bc1af3afd21d08d04aeb3ec53392fa664ca6d6c'
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
