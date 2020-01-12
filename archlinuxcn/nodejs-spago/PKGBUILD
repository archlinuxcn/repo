# Maintainer: csicar <aur@csicar.de>
_npmname=spago
_npmver=0.12.1
pkgname=nodejs-spago # All lowercase
pkgver=0.12.1
pkgrel=1
pkgdesc="PureScript package manager and build tool powered by Dhall and package-sets"
arch=(any)
url="https://github.com/spacchetti/spago"
license=(MIT)
depends=('nodejs' 'npm' 'purescript')
optdepends=()
source=(https://registry.npmjs.org/$_npmname/-/$_npmname-$_npmver.tgz)
noextract=($_npmname-$_npmver.tgz)
sha1sums=(18deb496c5da9c192217480aa846a55e6e1dbd5a)

package() {
  cd $srcdir
  local _npmdir="$pkgdir/usr/lib/node_modules/"
  mkdir -p $_npmdir
  cd $_npmdir
  npm install -g --prefix "$pkgdir/usr" $_npmname@$_npmver
}

# vim:set ts=2 sw=2 et:
