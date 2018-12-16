# Maintainer: Chih-Hsuan Yen <yan12125@gmail.com>

_npmname=web-ext
pkgname=nodejs-$_npmname
pkgver=2.9.3
pkgrel=1
pkgdesc='A command line tool to help build, run, and test web extensions'
arch=(any)
url='https://developer.mozilla.org/en-US/Add-ons/WebExtensions'
license=('MPL2')
depends=('nodejs')
makedepends=('yarn' 'node-gyp' 'python2' 'git')
# to speed up the build
options=('!strip')
# unit tests expect a git repo
source=("git+https://github.com/mozilla/web-ext.git#tag=$pkgver"
        exclude-scoped-modules.diff)
sha256sums=('SKIP'
            'badc28aad41212d3b08255298b48e43022f918a73e030a7f0245047cb9e33228')

prepare() {
  cd "$srcdir/$_npmname"
  patch -Np1 -i ../exclude-scoped-modules.diff

  cd "$srcdir"
  # -build for running webpack and tests, and the original for actual packaging
  cp -r $_npmname{,-build}
}

build() {
  cd "$srcdir/$_npmname-build"

  PYTHON=python2 yarn install
  NODE_ENV=production yarn run build
  cp -r dist "$srcdir/$_npmname"

  cd "$srcdir/$_npmname"
  PYTHON=python2 yarn install --production
}

check() {
  cd "$srcdir/$_npmname-build"

  yarn test
}

package() {
  local _npmdir="$pkgdir/usr/lib/node_modules/"

  install -Ddm755 "$_npmdir"
  cp -r --no-preserve=ownership $_npmname "$_npmdir/$_npmname"

  # remove references to $pkgdir
  rm -r "$_npmdir"/web-ext/node_modules/dtrace-provider/build/

  rm -r "$_npmdir"/web-ext/.git

  install -Ddm755 "$pkgdir/usr/bin"
  ln -s "/usr/lib/node_modules/$_npmname/bin/$_npmname" "$pkgdir/usr/bin/$_npmname"
}

# vim:set ts=2 sw=2 et:
