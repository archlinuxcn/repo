# Maintainer: Zenvie <134689569+Zenvie@users.noreply.github.com>
# Contributor: Felix Yan <felixonmars@archlinux.org>

pkgname=meta-rules-dat
pkgver=20240328
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
sha256sums=('6e0e73e3656b83f0fad9cb61a8f33b6c896e8cb1cb2db1502f0691640680fe88'
            '5519217f308e3f8f07fe8a8e695182064d0c835effd6ed20445d1b9a07625de2'
            '52475e5dd7f7d7f4f1dd2adf7bc51550d641a138ebe0aaae53585d4e58c3afbb'
            '2233357208b12f7747bde7be1f6baec0354a071abee7654c6a09cdbeb824de95')

prepare() {
  sha256sum -c *.dat.sha256sum
}

package() {  
  install -Dm644 -t "$pkgdir/etc/clash" *.dat
}
