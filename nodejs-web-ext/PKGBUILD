# Maintainer: Chih-Hsuan Yen <yan12125@gmail.com>

_npmname=web-ext
pkgname=nodejs-$_npmname
pkgver=2.9.1
pkgrel=3
pkgdesc='A command line tool to help build, run, and test web extensions'
arch=(any)
url='https://developer.mozilla.org/en-US/Add-ons/WebExtensions'
license=('MPL2')
depends=('nodejs')
makedepends=('yarn' 'node-gyp' 'python2')
# to speed up the build
options=('!strip')
source=(https://registry.npmjs.org/$_npmname/-/$_npmname-$pkgver.tgz)
sha256sums=('c9a0502df328f40a26457c31b59c3986497bec18d5f99c4272f7e2d6aa100ba8')

build() {
  cd package

  PYTHON=python2 yarn install --production
}

package() {
  local _npmdir="$pkgdir/usr/lib/node_modules/"

  install -Ddm755 "$_npmdir"
  cp -r --no-preserve=ownership package "$_npmdir/$_npmname"

  # remove references to $pkgdir
  rm -r "$pkgdir"/usr/lib/node_modules/web-ext/node_modules/dtrace-provider/build/

  install -Ddm755 "$pkgdir/usr/bin"
  ln -s "/usr/lib/node_modules/$_npmname/bin/$_npmname" "$pkgdir/usr/bin/$_npmname"
}

# vim:set ts=2 sw=2 et:
