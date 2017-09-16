# Maintainer: Anton Grensjö <anton@grensjo.se>
# Contributor: Vlad M. <vlad@archlinux.net>

_npmname=tiddlywiki
pkgname=nodejs-$_npmname
pkgver=5.1.14
pkgrel=1
pkgdesc="A non-linear personal web notebook"
url="http://tiddlywiki.com/"
arch=('any')
license=('BSD')
depends=('nodejs' 'npm')
source=(https://registry.npmjs.org/$_npmname/-/$_npmname-$pkgver.tgz)
noextract=($_npmname-$pkgver.tgz)
sha256sums=('6761e950c7c9140eda37208d11f0a9603edd12df566f214c9dbd41c3ba47c8d0')

package() {
  cd "$srcdir"
  local _npmdir="$pkgdir/usr/lib/node_modules/"
  mkdir -p "$_npmdir"
  cd "$_npmdir"
  npm install --user root -g --prefix "$pkgdir/usr" $_npmname@$pkgver
}
