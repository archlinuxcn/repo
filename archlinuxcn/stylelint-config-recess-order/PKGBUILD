# Maintainer: Zenvie <134689569+Zenvie@users.noreply.github.com>
# Contributor: Daniel M. Capella <polyzen@archlinux.org>

pkgname=stylelint-config-recess-order
pkgver=5.0.0
pkgrel=1
pkgdesc='Recess-based property sort order for Stylelint'
arch=(any)
url="https://github.com/stormwarning/$pkgname"
license=(ISC)
depends=(stylelint)
makedepends=(git)

prepare() {
  git clone --depth 1 --branch v$pkgver $url
}

package() {
  cd $pkgname
  install -Dm644 -t "$pkgdir/usr/lib/node_modules/$pkgname" {groups,index}.js\
    package.json
  install -Dm644 -t "$pkgdir/usr/share/doc/$pkgname" {CHANGELOG,README}.md
  install -Dm644 -t "$pkgdir/usr/share/licenses/$pkgname" LICENSE.txt
}
