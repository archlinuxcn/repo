# Maintainer: Kyle Keen <keenerd@gmail.com>
pkgname=pacgraph
pkgver=20110629
pkgrel=7
pkgdesc="Draws a graph of installed packages to PNG/SVG/GUI/console.  Good for finding bloat."
arch=('any')
url="http://kmkeen.com/pacgraph/"
license=('GPL')
depends=('python')
makedepends=()
optdepends=('inkscape: png backend'
            'imagemagick: png backend'
            'tk: gui version')
source=("http://kmkeen.com/pacgraph/$pkgname-$pkgver.tar.gz")
md5sums=('8f6da3a2fc4b8c5bb924767014b1cfb2')
sha256sums=('55c666d76cbf685f89c7242e44206a1b66922ea7d6394e8e19c9b9f189d349b6')

package() {
  cd "$srcdir/$pkgname"
  install -Dm0755 pacgraph    "$pkgdir/usr/bin/pacgraph"
  install -Dm0755 pacgraph-tk "$pkgdir/usr/bin/pacgraph-tk"
  install -Dm644  $pkgname.1  "$pkgdir/usr/share/man/man1/$pkgname.1"
}

