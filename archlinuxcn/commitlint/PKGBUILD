# Maintainer: Carl Smedstad <carsme@archlinux.org>
# Contributor: yochananmarqos
# Contributor: Thiago Almeida <thiagoalmeidasa@gmail.com>

pkgname=commitlint
pkgver=19.8.1
pkgrel=1
pkgdesc="Lint commit messages"
arch=(any)
url="https://github.com/conventional-changelog/commitlint"
license=(MIT)
depends=(nodejs)
makedepends=(npm)
optdepends=('commitlint-config-conventional: config enforcing conventional commits')
source=("https://registry.npmjs.org/$pkgname/-/$pkgname-$pkgver.tgz")
noextract=("$pkgname-$pkgver.tgz")
sha256sums=('b87082a3113be1c2929db63d727d3765b92f89e103b966996e7cfc560315ef68')

package() {
  npm install -g \
    --cache "$srcdir/npm-cache" \
    --prefix "$pkgdir/usr" \
    "$srcdir/$pkgname-$pkgver.tgz"

  install -Dm644 -t "$pkgdir/usr/share/licenses/$pkgname" \
    "$pkgdir/usr/lib/node_modules/$pkgname/license.md"

  # npm gives ownership of ALL FILES to build user
  # https://bugs.archlinux.org/task/63396
  chown -R root:root "$pkgdir"
}
