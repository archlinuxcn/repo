# Maintainer: Zenvie <134689569+Zenvie@users.noreply.github.com>
# Contributor: Daniel M. Capella <polyzen@archlinux.org>

pkgname=jslint.mjs
_pkgname=jslint
pkgver=2024.3.26
pkgrel=1
pkgdesc="The JavaScript Code Quality and Coverage Tool"
arch=(any)
url="https://github.com/jslint-org/$_pkgname"
license=(Unlicense)

depends=(nodejs)
makedepends=(npm)

source=("$_pkgname-$pkgver.tar.gz::$url/archive/refs/tags/v$pkgver.tar.gz")
sha256sums=('e57b21464e07efbe0395d0ff0040c1016f80552344c83b0a0d3a0d3613494283')

prepare() {
  cd "$_pkgname-$pkgver"
  npm install
}

check() {
  cd "$_pkgname-$pkgver"
  npm test
}

package() {
  cd "$_pkgname-$pkgver"
  sed -i 's|^// #!|#!|' "$pkgname"
  install -Dm755 "$pkgname" "$pkgdir/usr/bin/$pkgname"
}
