# Maintainer: Anton Grensjö <anton@grensjo.se>
# Contributor: Vlad M. <vlad@archlinux.net>

_npmname=tiddlywiki
pkgname=nodejs-$_npmname
pkgver=5.1.17
pkgrel=1
pkgdesc="A non-linear personal web notebook"
url="http://tiddlywiki.com/"
arch=('any')
license=('BSD')
depends=('nodejs' 'npm')
source=(https://registry.npmjs.org/$_npmname/-/$_npmname-$pkgver.tgz)
noextract=($_npmname-$pkgver.tgz)
sha256sums=('8c9c27f6599af265159b1258db4b22f8b2976cc0cfee5e2192aaa6363e0b2763')

package() {
  cd "$srcdir"
  local _npmdir="$pkgdir/usr/lib/node_modules/"
  mkdir -p "$_npmdir"
  cd "$_npmdir"
  npm install --user root -g --prefix "$pkgdir/usr" $_npmname@$pkgver
}
