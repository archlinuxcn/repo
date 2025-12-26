# Maintainer: Manuel Wiesinger <m {you know what belongs here} mmap {and here} at>

_ocamlname=parmap
pkgname=ocaml-${_ocamlname}
pkgver=1.2.5
pkgrel=1
pkgdesc="Minimalistic library allowing for multicore architectures"
arch=('x86_64')
url="https://rdicosmo.github.io/parmap"
license=('LGPL-2.1-or-later')
depends=('glibc' 'ocaml')
makedepends=('dune')
source=("${pkgname}-${pkgver}.tar.gz::https://github.com/rdicosmo/parmap/archive/refs/tags/${pkgver}.tar.gz")
b2sums=('6e6c5c7dcfd1e7af4b921bc8795b2a23f0fd5e01f6ce91665bbbc5e1f9e19f0b7eaee0361b3450d4a9823744c97c6f6ef28f8c8f1f65fad80f2a0a30dc07b740')
options=('!strip')

build() {
    cd $srcdir/$_ocamlname-$pkgver
    dune build -p $_ocamlname
}

check() {
    cd $srcdir/$_ocamlname-$pkgver
    dune test
}

package() {
    cd $srcdir/$_ocamlname-$pkgver
    DESTDIR=$pkgdir dune install --prefix "/usr" --libdir "/usr/lib/ocaml" --docdir "/usr/share/doc"

    install -d  $pkgdir/usr/share/licenses/$pkgname/
    mv $pkgdir/usr/share/doc/$_ocamlname/LICENSE $pkgdir/usr/share/licenses/$pkgname/

    # TODO docs, requires ocaml-odoc package
}
