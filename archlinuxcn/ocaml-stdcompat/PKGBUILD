# Maintainer: Manuel Wiesinger <m {you know what belongs here} mmap {and here} at>

_ocamlname=stdcompat
pkgname=ocaml-$_ocamlname
pkgver=21.1
pkgrel=2
pkgdesc="Compatibility module for OCaml standard library"
url="https://github.com/thierry-martinez/stdcompat"
license=('LGPL-2.1-or-later')
source=(
    "$pkgname-$pkgver.tar.gz::https://github.com/thierry-martinez/stdcompat/archive/refs/tags/${pkgver}.tar.gz"
    "0000-fedora-ocaml-stdcompat-ocaml5.4.patch::https://src.fedoraproject.org/rpms/ocaml-stdcompat/raw/2f4345ccea8eda0cd2a4cc33c337a9d92d66eb3c/f/ocaml-stdcompat-ocaml5.4.patch")
depends=('ocaml')
makedepends=('dune')
arch=('x86_64')
b2sums=('b351696f0aed268cd067e20a7d0917a5580399b43e5de3e60fce0ab30a8093cd1808eda610d5a20eb721033f77c45f9b5c8dabc6d55862b023c363b212a505e8'
        '6e1a1f533977af92a3139a1acb6a8aaeaff2c1b12ca14bccb435d2ffaa8abf427a5da8dff172fc445d4f152e5c8a06d142ada7765a548149fb80d653ec0f8345')

prepare() {
    cd "${srcdir}/${_ocamlname}-${pkgver}"
    patch --forward --strip=1 --input=../0000-fedora-ocaml-stdcompat-ocaml5.4.patch
}

build() {
    cd "${srcdir}/${_ocamlname}-${pkgver}"
    dune build --ignore-promoted-rules
}

check() {
    cd "${srcdir}/${_ocamlname}-${pkgver}"
    dune test
}

package() {
    cd "${srcdir}/${_ocamlname}-${pkgver}"

    DESTDIR=$pkgdir \
	dune install -p stdcompat \
	--prefix "/usr" \
	--libdir "/usr/lib/ocaml" \
	--docdir "/usr/share/doc"

    install -Dm644 README.md -t $pkgdir/usr/share/doc/$pkgname/
    install -Dm644 CHANGES.md -t $pkgdir/usr/share/doc/$pkgname/

    rm -f $pkgdir/usr/share/doc/$_ocamlname/README.md
    rm -f $pkgdir/usr/share/doc/$_ocamlname/CHANGES.md
    rmdir $pkgdir/usr/share/doc/$_ocamlname
}
