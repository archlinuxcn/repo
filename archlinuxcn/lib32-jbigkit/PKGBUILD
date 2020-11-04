# Maintainer: Rodrigo Bezerra <rodrigobezerra21 at gmail dot com>

_basename=jbigkit
pkgname=lib32-jbigkit
pkgver=2.1
pkgrel=1
pkgdesc="Data compression library/utilities for bi-level high-resolution images (32-bit)"
arch=('x86_64')
url="http://www.cl.cam.ac.uk/~mgk25/jbigkit/"
license=('GPL')
depends=('jbigkit')
options=('staticlibs')
source=(https://www.cl.cam.ac.uk/~mgk25/download/jbigkit-$pkgver.tar.gz)
sha256sums=('de7106b6bfaf495d6865c7dd7ac6ca1381bd12e0d81405ea81e7f2167263d932')

build() {
    cd "$_basename-$pkgver"

    unset CFLAGS CPPFLAGS LDFLAGS CC
    [ "$CARCH" == "x86_64" ] && export CFLAGS="$CFLAGS -fPIC" CC='gcc -m32'

    make CFLAGS="$CFLAGS" CC="$CC"
}

package() {
    cd "$_basename-$pkgver"

    install -D -m644 libjbig/libjbig.a "$pkgdir"/usr/lib32/libjbig.a
    install -D -m644 libjbig/libjbig85.a "$pkgdir"/usr/lib32/libjbig85.a
}
