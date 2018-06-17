# Maintainer: Hans-Nikolai Viessmann <hv15 AT hw.ac.uk>
# Category: science
pkgname=('polylib' 'polylib-gmp')
pkgbase='polylib'
pkgver='5.22.5'
pkgrel=5
pkgdesc='A library of polyhedral functions'
arch=('i686' 'x86_64')
url='http://icps.u-strasbg.fr/polylib/'
license=('GPL')
depends=('gmp')
source=("http://icps.u-strasbg.fr/polylib/polylib_src/$pkgname-$pkgver.tar.gz")
md5sums=('c0088786e0a5ae64b7cc47ad19ae4f83')

build() {
    cd "$srcdir/$pkgbase-$pkgver"

    # now we build the normal version of polylib
    echo "compiling normal version of Polylib"
    [ -d "polylib" ] || mkdir "polylib"
    cd polylib
    ../configure --prefix=/usr
    make

    cd ..
    # now we build the GMP version of polylib
    echo "compiling GMP version of Polylib"
    [ -d "polylibgmp" ] || mkdir "polylibgmp"
    cd polylibgmp
    ../configure --prefix=/usr --with-libgmp
    make
}

check() {
    cd "$srcdir/$pkgbase-$pkgver"

    # check the normal version
    cd polylib
    make check

    cd ..
    # check the GMP version
    cd polylibgmp
    make check
}

package_polylib() {
    cd "$srcdir/$pkgbase-$pkgver/polylib"
    make DESTDIR="$pkgdir" install
}

package_polylib-gmp() {
    depends=("polylib>=$pkgver")

    cd "$srcdir/$pkgbase-$pkgver/polylibgmp"
    make DESTDIR="$pkgdir" install-exec
   
    cd "$pkgdir"
    # Nasty rename to ensure we can co-exist with polylib
    mv usr/bin/c2p usr/bin/c2p-gmp
    mv usr/bin/disjoint_union_adj usr/bin/disjoint_union_adj-gmp
    mv usr/bin/disjoint_union_sep usr/bin/disjoint_union_sep-gmp
    mv usr/bin/ehrhart_lower_bound usr/bin/ehrhart_lower_bound-gmp
    mv usr/bin/ehrhart_quick_apx usr/bin/ehrhart_quick_apx-gmp
    mv usr/bin/ehrhart_upper_bound usr/bin/ehrhart_upper_bound-gmp
    mv usr/bin/findv usr/bin/findv-gmp
    mv usr/bin/r2p usr/bin/r2p-gmp
}
