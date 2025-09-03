# Maintainer: Kiri <kiri@vern.cc>
# Contributor: Zenvie <134689569+Zenvie@users.noreply.github.com>
# Contributor: Felix Yan <felixonmars@archlinux.org>

pkgname=meta-rules-dat
pkgver=20250903
pkgver() {
  date +'%Y%m%d'
}
pkgrel=1
pkgdesc="rules dat files by MetaCubeX"
arch=(any)
url="https://github.com/MetaCubeX/$pkgname"
license=(CC-BY-SA-4.0 GPL-2.0-or-later GPL-3.0-or-later)

source=("$url/raw/release/geoip.dat"
        "$url/raw/release/geosite.dat"
        "$url/raw/release/geoip.dat.sha256sum"
        "$url/raw/release/geosite.dat.sha256sum")
sha256sums=('SKIP'
            'SKIP'
            'SKIP'
            'SKIP')

prepare() {
  sha256sum -c *.dat.sha256sum
}

package() {  
  install -Dm644 -t "$pkgdir/etc/clash" *.dat
}
