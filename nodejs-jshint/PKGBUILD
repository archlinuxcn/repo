# Maintainer: John D Jones III AKA jnbek <jnbek1972 -_AT_- g m a i l -_Dot_- com>
_npmname=jshint
_npmver=2.9.2
pkgname=nodejs-jshint # All lowercase
pkgver=2.9.2
pkgrel=1
pkgdesc="Static analysis tool for JavaScript"
arch=(any)
url="http://jshint.com/"
license=(MIT)
depends=('nodejs' 'npm')
optdepends=()
source=(https://registry.npmjs.org/$_npmname/-/$_npmname-$_npmver.tgz)
noextract=($_npmname-$_npmver.tgz)
sha1sums=('0b12d75f8eafb0823b7bf8efbb265b3262401619')

package() {
  cd "$srcdir"
  local _npmdir="$pkgdir/usr/lib/node_modules/"
  mkdir -p "$_npmdir"
  cd "$_npmdir"
  npm install --user root -g --prefix "$pkgdir/usr" $_npmname@$_npmver
}
