_npmname=gitbook-cli
_npmver=2.2.0
pkgname=nodejs-gitbook-cli # All lowercase
pkgver="$_npmver"
pkgrel=1
pkgdesc="CLI to generate books and documentation using gitbook"
arch=(any)
url="https://www.gitbook.com"
license=()
depends=('nodejs' 'npm' )
optdepends=()
source=(http://registry.npmjs.org/$_npmname/-/$_npmname-$_npmver.tgz)
noextract=($_npmname-$_npmver.tgz)
sha1sums=('c02697d85179df90d259050d949b57f03b631fbf')

package() {
  cd $srcdir
  local _npmdir="$pkgdir/usr/lib/node_modules/"
  mkdir -p $_npmdir
  cd $_npmdir
  npm install -g --prefix "$pkgdir/usr" $_npmname@$_npmver
}

# vim:set ts=2 sw=2 et:
