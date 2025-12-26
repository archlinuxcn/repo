# Maintainer: Manuel Wiesinger <m {you know what belongs here} mmap {and here} at>
# Contributor: Eric Fung <loseurmarbles[at]gmail[dot]com>
# Contributor: Jakob Gahde <j5lx@fmail.co.uk>
# Contributor: Leonard de Ruijter <leonard@aur.archlinux.org>
# Contributor: Serge Zirukin <ftrvxmtrx@gmail.com>
# Contributor: Sergei Lebedev <superbobry@gmail.com>
# Contributor: Magnus Therning <magnus@therning.org>

_ocamlname=pcre
pkgname=ocaml-$_ocamlname
pkgver=8.0.5
pkgrel=1
pkgdesc="Perl compatible regular expressions for OCaml"
arch=('x86_64')
url="http://mmottl.github.io/pcre-ocaml"
license=('LicenseRef-LGPL2.1-with-OCaml-LGPL-linking-exception')
depends=('glibc' 'ocaml-base' 'ocaml-findlib' 'pcre')
makedepends=('dune' 'ocaml-ounit')
provides=('pcre-ocaml')
replaces=('pcre-ocaml')
conflicts=('pcre-ocaml')
options=('!strip' 'staticlibs' '!debug')
source=("$pkgname-$pkgver.tar.gz::https://github.com/mmottl/pcre-ocaml/releases/download/${pkgver}/pcre-${pkgver}.tbz")
b2sums=('309fb9fe13d4be8ee15e5fa96c081485e91e8ecd1c2109df3856499a01256236cdb8288d849a386e49ad86b7df98197137d43403ad1f1ac899901fe34c8ff762')


build() {
    cd "${srcdir}/pcre-${pkgver}"

    export OCAMLPATH="$(ocamlfind printconf destdir)"
    dune build -p $_ocamlname
}

check() {
    cd "${srcdir}/pcre-${pkgver}"
    dune runtest --verbose
}

package() {
    cd "${srcdir}/pcre-${pkgver}"

    dune install \
	 --destdir="${pkgdir}" \
	 --prefix="/usr" \
	 --docdir="/usr/share/doc" \
	 --libdir="$(ocamlfind printconf destdir)"

    # TODO
    #  - doc needs an odoc package

    mv "${pkgdir}/usr/share/doc/pcre" "${pkgdir}/usr/share/doc/${pkgname}"

    install -d "${pkgdir}/usr/share/licenses/${pkgname}"
    mv "${pkgdir}/usr/share/doc/${pkgname}/LICENSE.md" "${pkgdir}/usr/share/licenses/${pkgname}"
}
