# Maintainer: Anton Grensjö <anton@grensjo.se>
# Contributor: Vlad M. <vlad@archlinux.net>

_npmname=tiddlywiki
pkgname=nodejs-$_npmname
pkgver=5.1.13
pkgrel=1
pkgdesc="A non-linear personal web notebook"
url="http://tiddlywiki.com/"
arch=('any')
license=('BSD')
depends=('nodejs' 'npm')
source=(https://registry.npmjs.org/$_npmname/-/$_npmname-$pkgver.tgz)
noextract=($_npmname-$pkgver.tgz)
sha256sums=('36f23307411c35da907854366ae85ebe037ebc728bd6b15974ca375838889895')

package() {
  cd "$srcdir"
  local _npmdir="$pkgdir/usr/lib/node_modules/"
  mkdir -p "$_npmdir"
  cd "$_npmdir"
  npm install --user root -g --prefix "$pkgdir/usr" $_npmname@$pkgver
}
