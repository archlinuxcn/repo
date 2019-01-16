# Maintainer: Hans-Nikolai Viessmann <hans AT viess.mn>
pkgname='barvinok'
pkgver=0.41
pkgrel=1
pkgdesc='A library for counting the number of integer points in parametric and non-parametric polytopes'
arch=('x86_64')
url='http://freecode.com/projects/barvinok'
license=('GPL')
depends=('ntl' 'isl>0.17' 'polylib-gmp')
source=("http://barvinok.gforge.inria.fr/$pkgname-$pkgver.tar.xz"
        'fix-missing-isl-include.patch')
md5sums=('a5496a4a93f3f1f26fef07189e12314f'
         '44a312463a5688031d26e615b8a22594')

prepare() {
    cd "$srcdir/$pkgname-$pkgver"

    # because we are building with system ISL, we need to correct a minor oversight, which
    # is that a dummy library is generated to wrap around all the ISL functions - for bundled
    # or build case, the linking is handled correctly. For system case the linking does not
    # include the correct include path. This patch adds the missing include path.
    patch -p0 < ../fix-missing-isl-include.patch

    # rebuild autotools
    autoconf -i
}

build() {
    cd "$srcdir/$pkgname-$pkgver"

    # NTL 11 now uses pthread functions, so we need to have it link to libpthread.
    ./configure --prefix=/usr --enable-shared-barvinok --with-isl=system --with-polylib=system LIBS="-lpthread"
    make
}

check() {
    cd "$srcdir/$pkgname-$pkgver"
    make check
}

package() {
    cd "$srcdir/$pkgname-$pkgver"
    make DESTDIR="$pkgdir" install
}
