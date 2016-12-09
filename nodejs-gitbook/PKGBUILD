# Maintainer: SY.Zhang  <lastavenger#archlinuxcn.org>
# Contributor: Will Price <will.price94@gmail.com>

_npmname=gitbook
_npmver=3.2.2
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
sha256sums=('7424da266d9878dd80a1c99b8e1bc12b94bf7cfc3933ff62f6d86639d63c4f21'
            '52743d4e3212c100aca0afc2021255967ce1c8e6f07f630851470fa38114558e')

package() {
  cd $srcdir
  local _npmdir="$pkgdir/usr/lib/node_modules/"
  mkdir -p $_npmdir
  cd $_npmdir
  npm install --user root -g --prefix "$pkgdir/usr" $_npmname@$_npmver
  npm install --user root -g --prefix "$pkgdir/usr" $_npmname2@$_npmver2
}

# vim:set ts=2 sw=2 et:
