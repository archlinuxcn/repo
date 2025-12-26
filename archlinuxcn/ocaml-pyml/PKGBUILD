# Maintainer: Manuel Wiesinger <m {you know what belongs here} mmap {and here} at>

_ocamlname=pyml
pkgname=ocaml-$_ocamlname
pkgver=20250807
pkgrel=1
pkgdesc="OCaml bindings for Python 2 and Python 3"
arch=('x86_64')
url="https://github.com/ocamllibs/pyml"
license=('BSD-2-Clause')
depends=('glibc' 'ocaml' 'python')
makedepends=('dune' 'ocaml-stdcompat')
source=("$pkgname-$pkgver.tar.gz::https://github.com/ocamllibs/pyml/archive/refs/tags/20250807.tar.gz")
b2sums=('279c3ed46babc79114051426494b2fe83d1abec634e5e798b48d6f60889b7b29eaaf353d4655a50610cf82c0c11922d1bfa633d608087b51cb7ac8fe27be6470')
options=('!strip')

build() {
    cd "${srcdir}/${_ocamlname}-${pkgver}"
    dune build --release --verbose
}

check() {
    cd "${srcdir}/${_ocamlname}-${pkgver}"
    dune runtest --release --verbose
}

package() {
    cd "${srcdir}/${_ocamlname}-${pkgver}"

    DESTDIR="${pkgdir}" dune install \
	   --prefix "/usr" \
	   --libdir "/usr/lib/ocaml" \
	   --docdir "/usr/share/doc"

    install -d -m755 "${pkgdir}/usr/share/licenses/${pkgname}/"
    mv "${pkgdir}/usr/share/doc/pyml/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/"
}
