# Maintainer: Carl Smedstad <carl.smedstad at protonmail dot com>
# Contributor: yochananmarqos
# Contributor: Thiago Almeida <thiagoalmeidasa@gmail.com>

pkgname=commitlint
pkgver=19.2.1
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
sha256sums=('680a6a30a95eb2dcacfe9c7916d7ed604c678fcfcbb366f9970edb32e4b1348f')

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
