# Maintainer: csicar <aur@csicar.de>
_npmname=spago
_npmver=0.16.0
pkgname=nodejs-spago
pkgver=0.16.0
pkgrel=1
pkgdesc="PureScript package manager and build tool powered by Dhall and package-sets"
arch=(any)
url="https://github.com/spacchetti/spago"
license=(MIT)
depends=('nodejs' 'npm' 'purescript' 'ncurses5-compat-libs')
optdepends=()
source=(https://registry.npmjs.org/$_npmname/-/$_npmname-$_npmver.tgz)
noextract=($_npmname-$_npmver.tgz)
sha256sums=(1c054f1a8ae5c44e374ce816df76d79c5aae10d6231d5b7bb2c63eb6ab1b6301)

package() {
  cd $srcdir
  local _npmdir="$pkgdir/usr/lib/node_modules/"
  mkdir -p $_npmdir
  cd $_npmdir
  npm install -g --prefix "$pkgdir/usr" $_npmname@$_npmver
}

# vim:set ts=2 sw=2 et:
