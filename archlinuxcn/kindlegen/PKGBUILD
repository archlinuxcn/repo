# Contributor: Valentin-Costel Haloiu <vially.ichb@gmail.com>
# Contributor: Eugene Yunak <e.yunak@gmail.com>
# Contributor: Pellegrino Prevete <pellegrinoprevete@gmail.com>

pkgname=kindlegen
pkgver=2.9
pkgrel=5
pkgdesc="A command line tool used to build eBooks that can be sold through Amazon's Kindle platform."
arch=('i686' 'x86_64')
url="https://www.amazon.com/gp/feature.html?ie=UTF8&docId=1000765211"
license=(custom)
source=("https://archive.org/download/kindlegen/kindlegen")
sha256sums=('b8b0f0ab83e74070119066bf4f3c56267e5ee43d2c2bac7091bb447e9f461a69')

package() {
    install -D -m755 $srcdir/kindlegen $pkgdir/usr/bin/kindlegen

}
