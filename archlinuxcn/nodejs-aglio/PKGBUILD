# Maintainer: Kevin Houdebert <kevin@qwazerty.eu>

_npmname=aglio
_npmver=2.3.0
pkgname=nodejs-aglio # All lowercase
pkgver=2.3.0
pkgrel=1
pkgdesc="An API Blueprint renderer with theme support that outputs static HTML"
arch=(any)
url="https://github.com/danielgtaylor/aglio"
license=()
depends=('nodejs' 'npm')
optdepends=()
source=(http://registry.npmjs.org/$_npmname/-/$_npmname-$_npmver.tgz)
noextract=($_npmname-$_npmver.tgz)
sha256sums=('521b860ac4795a0e9f1f66dac63a222d4c9e15c6914381cad1082ee41ee6cedc')

package() {
  cd "$srcdir"
  local _npmdir="$pkgdir/usr/lib/node_modules/"
  mkdir -p "$_npmdir"
  cd "$_npmdir"
  npm install -g --prefix "$pkgdir/usr" $_npmname@$_npmver
}

# vim:set ts=2 sw=2 et:
