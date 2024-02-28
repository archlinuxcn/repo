# Maintainer: Carl Smedstad <carl.smedstad at protonmail dot com>
# Contributor: yochananmarqos
# Contributor: Thiago Almeida <thiagoalmeidasa@gmail.com>

pkgname=commitlint
pkgver=19.0.3
pkgrel=1
pkgdesc="Lint commit messages"
arch=(any)
url="https://github.com/conventional-changelog/commitlint"
license=(MIT)
depends=(nodejs)
makedepends=(npm)
source=(
  "https://registry.npmjs.org/$pkgname/-/$pkgname-$pkgver.tgz"
  "https://registry.npmjs.org/@commitlint/config-conventional/-/config-conventional-$pkgver.tgz"
)
noextract=(
  "$pkgname-$pkgver.tgz"
  "config-conventional-$pkgver.tgz"
)
sha256sums=(
  '857d1cbe8116af57a9f0fe964e8ea0419bd7f76f2d02363eeb81b7005ebc795a'
  'c3128d3f612d8ebfea260006e11841bfc8ef570c56ccd8aa5cdd9b0dfac74a27'
)

package() {
  npm install -g \
    --cache "$srcdir/npm-cache" \
    --prefix "$pkgdir/usr" \
    "$srcdir/$pkgname-$pkgver.tgz"
  npm install -g \
    --cache "$srcdir/npm-cache" \
    --prefix "$pkgdir/usr" \
    "$srcdir/config-conventional-$pkgver.tgz"

  install -Dm644 -t "$pkgdir/usr/share/licenses/$pkgname" \
    "$pkgdir/usr/lib/node_modules/$pkgname/license.md"

  # npm gives ownership of ALL FILES to build user
  # https://bugs.archlinux.org/task/63396
  chown -R root:root "$pkgdir"
}
