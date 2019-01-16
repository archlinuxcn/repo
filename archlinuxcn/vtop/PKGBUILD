_npmname=vtop
_npmver=0.6.1
pkgname=$_npmname # All lowercase
pkgver=$_npmver
pkgrel=1
pkgdesc="Wow such top. So stats"
arch=(any)
url="http://parall.ax/vtop"
license=()
depends=('nodejs')
makedepends=('npm')
source=(http://registry.npmjs.org/$_npmname/-/$_npmname-$_npmver.tgz)
noextract=($_npmname-$_npmver.tgz)
sha1sums=('ee1098505f3300e762a7e663455c6fa68be07fbf')

package() {
  cd $srcdir
  local _npmdir="$pkgdir/usr/lib/node_modules/"
  mkdir -p $_npmdir
  cd $_npmdir
  npm install -g --prefix "$pkgdir/usr" $_npmname@$_npmver
}

# vim:set ts=2 sw=2 et:
