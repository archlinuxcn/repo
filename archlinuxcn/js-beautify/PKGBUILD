# Maintainer: Arnau Sanchez <pyarnau@gmail.com>
_npmname=js-beautify
_npmver=1.7.5
pkgname=js-beautify # All lowercase
pkgver=$_npmver
pkgrel=2
pkgdesc="Beautify JavaScript/JSON (jsbeautifier.org)"
arch=(any)
license=('MIT')
url="http://jsbeautifier.org/"
depends=('nodejs')
makedepends=('npm')
conflicts=('python-jsbeautifier')
source=(http://registry.npmjs.org/$_npmname/-/$_npmname-$_npmver.tgz)
noextract=($_npmname-$_npmver.tgz)
md5sums=(9ee13ddfc42482f91a661c5dde4348cc)

package() {
  cd $srcdir
  local _npmdir="$pkgdir/usr/lib/node_modules/"
  mkdir -p $_npmdir
  cd $_npmdir
  npm install -g --prefix "$pkgdir/usr" $_npmname@$_npmver
}

# vim:set ts=2 sw=2 et:
