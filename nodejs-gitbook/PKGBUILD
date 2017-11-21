# Maintainer: Shengyu Zhang <la@archlinuxcn.org>
# Contributor: Will Price <will.price94@gmail.com>

_npmname=gitbook
_npmver=3.2.2
_npmname2=gitbook-cli
_npmver2=2.3.2
pkgname=nodejs-$_npmname
pkgver=$_npmver
pkgrel=4
pkgdesc='Library and cmd utility to generate GitBooks'
arch=(any)
url='http://www.gitbook.io/'
license=()
makedepends=('npm' 'git')
depends=('nodejs')
optdepends=('nodejs-svgexport: SVG support')
provides=('nodejs-gitbook')
conflicts=('nodejs-gitbook-cli')
source=("http://registry.npmjs.org/$_npmname/-/$_npmname-$_npmver.tgz"
        "http://registry.npmjs.org/$_npmname2/-/$_npmname2-$_npmver2.tgz")
noextract=("$_npmname-$_npmver.tgz"
           "$_npmname2-$_npmver2.tgz")
sha256sums=('7424da266d9878dd80a1c99b8e1bc12b94bf7cfc3933ff62f6d86639d63c4f21'
            'e11af44f5d5b4491b242e81b1b3bffd356164ae7b46f4dbc21746cf8e07bac90')

package() {
  cd $srcdir
  local _npmdir="$pkgdir/usr/lib/node_modules/"
  mkdir -p $_npmdir
  cd $_npmdir
  npm install --user root -g --prefix "$pkgdir/usr" $_npmname@$_npmver
  npm install --user root -g --prefix "$pkgdir/usr" $_npmname2@$_npmver2

  chmod 755 $_npmdir$_npmname
}

# vim:set ts=2 sw=2 et:
