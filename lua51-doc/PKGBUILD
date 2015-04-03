# Maintainer:
# Contributor: Chris Brannon <cmbrannon79@gmail.com>
# Contributor: Paulo Matias <matiasΘarchlinux-br·org>

pkgname=lua51-doc
pkgver=3.0.1
pkgrel=2
pkgdesc='Documentation generator tool for Lua source code'
arch=('any')
url='http://luadoc.luaforge.net'
license=('MIT')
makedepends=('lua51' 'lua51-filesystem' 'lua51-logging')
depends=('lua51' 'lua51-filesystem' 'lua51-logging')
replaces=('luadoc')
conflicts=('luadoc')
source=("http://luaforge.net/frs/download.php/3185/luadoc-$pkgver.tar.gz"
        'LICENSE')
md5sums=('ec3a0c0b9413e401a2d466cc0930d505'
         'c2a5289bdfe3702fd77b365a48251c08')

prepare() {
  find luadoc-$pkgver -type f -exec \
    sed -i '1s,^#! \?/usr/bin/\(env \|\)lua$,#!/usr/bin/lua5.1,' {} \;
}

package() {
  cd "luadoc-$pkgver"

  make PREFIX="$pkgdir/usr" install
  install -Dm644 "$srcdir/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}

# vim:set ts=2 sw=2 et:
