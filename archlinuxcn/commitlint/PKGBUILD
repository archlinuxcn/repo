# Maintainer: Carl Smedstad <carl.smedstad at protonmail dot com>
# Contributor: yochananmarqos
# Contributor: Thiago Almeida <thiagoalmeidasa@gmail.com>

pkgname=commitlint
pkgver=19.1.0
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
  '31488ca805d13b23e50bc611d4dd268f88473699bd4e5c5bd59873d2d2f69175'
  '7ade13700dd3f7af4bc0e1a15cf755874420e6662668c5ba8163896fce95a19b'
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
