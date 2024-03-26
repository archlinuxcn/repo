# Maintainer: Zenvie <134689569+Zenvie@users.noreply.github.com>
# Contributor: Daniel M. Capella <polyzen@archlinux.org>

pkgname=stylelint-config-recess-order
pkgver=5.0.0
pkgrel=3
pkgdesc="Recess-based property sort order for Stylelint"
arch=(any)
url="https://github.com/stormwarning/$pkgname"
license=(ISC)

depends=(stylelint)
makedepends=(npm)

source=("$pkgname-$pkgver.tar.gz::$url/archive/refs/tags/v$pkgver.tar.gz")
sha256sums=('6616f3729be9e5b2f778fd72677879cd40b6f6fac9046108c5ead6363c96800b')

prepare() {
  cd $pkgname-$pkgver
  npm install
}

check() {
  cd $pkgname-$pkgver
  npm test
}

package() {
  cd $pkgname-$pkgver
  install -Dm644 -t "$pkgdir/usr/lib/node_modules/$pkgname" {groups,index}.js package.json
  install -Dm644 -t "$pkgdir/usr/share/doc/$pkgname" {CHANGELOG,README}.md
  install -Dm644 -t "$pkgdir/usr/share/licenses/$pkgname" LICENSE.txt
}
