# Maintainer: marcs <aur@mg.odd.red>

_npmname=vue-cli
_npmver=2.9.6
pkgname=nodejs-vue-cli # All lowercase
pkgver=2.9.6
pkgrel=1
pkgdesc="A simple CLI for scaffolding Vue.js projects."
arch=(any)
url="https://github.com/vuejs/vue-cli#readme"
license=()
depends=('nodejs' 'npm' )
optdepends=()
source=(http://registry.npmjs.org/$_npmname/-/$_npmname-$_npmver.tgz)
noextract=($_npmname-$_npmver.tgz)
sha1sums=('afc3cc6ce6de350d89876fee2dc163d0b83e0136')

package() {
  cd $srcdir
  local _npmdir="$pkgdir/usr/lib/node_modules/"
  mkdir -p $_npmdir
  cd $_npmdir
  npm install -g --prefix "$pkgdir/usr" $_npmname@$_npmver

  # permission fix
  chmod 755 ${pkgdir}/usr/bin
}

# vim:set ts=2 sw=2 et:
