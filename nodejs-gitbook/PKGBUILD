# Maintainer: SY.Zhang  <lastavengers#outlook.com>
# Contributor: Will Price <will.price94@gmail.com>

_npmname=gitbook
_npmver=2.3.1
_npmname2=gitbook-cli
_npmver2=2.3.0
pkgname=nodejs-$_npmname
pkgver=$_npmver
pkgrel=2
pkgdesc='Library and cmd utility to generate GitBooks'
arch=(any)
url='http://www.gitbook.io/'
license=()
makedepends=('npm' 'git')
depends=('nodejs')
provides=('nodejs-gitbook')
conflicts=('nodejs-gitbook-cli')
source=("http://registry.npmjs.org/$_npmname/-/$_npmname-$_npmver.tgz"
        "http://registry.npmjs.org/$_npmname2/-/$_npmname2-$_npmver2.tgz")
noextract=("$_npmname-$_npmver.tgz"
           "$_npmname2-$_npmver2.tgz")
sha256sums=('851de325a3badef58ba8abcee2f867f62e9ef81e95b93ce82ea4954f28eff1f9'
            'SKIP')

package() {
  cd $srcdir
  local _npmdir="$pkgdir/usr/lib/node_modules/"
  mkdir -p $_npmdir
  cd $_npmdir
  npm install -g --prefix "$pkgdir/usr" $_npmname@$_npmver
  npm install -g --prefix "$pkgdir/usr" $_npmname2@$_npmver2
}

# vim:set ts=2 sw=2 et:
