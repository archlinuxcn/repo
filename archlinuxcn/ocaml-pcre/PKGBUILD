# Maintainer: Manuel Wiesinger <m {you know what belongs here} mmap {and here} at>
# Contributor: Eric Fung <loseurmarbles[at]gmail[dot]com>
# Contributor: Jakob Gahde <j5lx@fmail.co.uk>
# Contributor: Leonard de Ruijter <leonard@aur.archlinux.org>
# Contributor: Serge Zirukin <ftrvxmtrx@gmail.com>
# Contributor: Sergei Lebedev <superbobry@gmail.com>
# Contributor: Magnus Therning <magnus@therning.org>

_ocamlname=pcre
pkgname=ocaml-$_ocamlname
pkgver=8.0.3
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
b2sums=('0df11589bb803d3bf6d2f3172bf3f9e3d0856749a3e7f18c24920e909e35eff935f5e3ec5a00c2f4e0240de672ec53dc45093fb1b10a580baf42bf87f38ca866')


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
