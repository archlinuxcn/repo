# Maintainer: Zenvie <134689569+Zenvie@users.noreply.github.com>
# Contributor: Felix Yan <felixonmars@archlinux.org>

pkgname=jslint.mjs
_pkgname=jslint
pkgver=2023.10.24
pkgrel=1
pkgdesc="The JavaScript Code Quality and Coverage Tool"
arch=(any)
url="https://github.com/jslint-org/$_pkgname"
license=(Unlicense)
depends=(nodejs)
source=("$_pkgname-$pkgver.tar.gz::$url/archive/refs/tags/v$pkgver.tar.gz")
sha256sums=('c49ffc67a79980fc6e401e6bb81170f74e475080f15f201c1a98f1892d6f41ea')

package() {
  cd "$_pkgname-$pkgver"
  sed -i 's|^// #!|#!|' "$pkgname"
  install -Dm755 "$pkgname" "$pkgdir/usr/bin/$pkgname"
}
