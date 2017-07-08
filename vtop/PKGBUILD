_npmname=vtop
_npmver=0.5.7
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
sha1sums=('fff91000fac3a97a165f6f52dc253bce3d4d091e')

package() {
  cd $srcdir
  local _npmdir="$pkgdir/usr/lib/node_modules/"
  mkdir -p $_npmdir
  cd $_npmdir
  npm install -g --prefix "$pkgdir/usr" $_npmname@$_npmver
}

# vim:set ts=2 sw=2 et:
