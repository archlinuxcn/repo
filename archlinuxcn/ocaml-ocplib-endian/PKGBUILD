# Maintainer: Daniel Peukert <daniel@peukert.cc>
# Contributor: Jakob Gahde <j5lx@fmail.co.uk>
_projectname='ocplib-endian'
pkgname="ocaml-$_projectname"
pkgver='1.2'
pkgrel='9'
pkgdesc='Optimised functions to read and write int16/32/64 from strings, bytes and bigarrays'
arch=('x86_64' 'aarch64')
url="https://github.com/OCamlPro/$_projectname"
license=('LGPL-2.1-or-later WITH OCaml-LGPL-linking-exception')
depends=('ocaml>=4.03.0')
makedepends=('cppo' 'dune>=1.0.0')
options=('!strip')
source=(
	"$pkgname-$pkgver.tar.gz::$url/archive/$pkgver.tar.gz"
	"$pkgname-$pkgver-remove-bytes-dep.diff::$url/pull/26.diff"
)
b2sums=('25354888f80ec4d09b9605f293b121dd66d365a461d2e40d9c3d41afa56303562d5db03a469469c1d59d304dd0d47657381c2f42b9e4935005c2ce85fbd5b80a'
        'ecc218f13bf8c17f9c2b793f961936f26d4e2cb0d0490cae362dbf494e53fcbbf6ed511c2299f7ca55077e32ec766e0dcd4a5329e275ed97143931a1c1672867')

_sourcedirectory="$_projectname-$pkgver"

prepare() {
	cd "$srcdir/$_sourcedirectory/"

	# Make sure we don't directly depend on bytes, as that stopped working in ocaml 5.0 (https://github.com/OCamlPro/ocplib-endian/pull/26)
	patch --forward -p1 < "../$pkgname-$pkgver-remove-bytes-dep.diff"
}

build() {
	cd "$srcdir/$_sourcedirectory/"
	dune build --release --verbose
}

check() {
	cd "$srcdir/$_sourcedirectory/"
	dune runtest --release --verbose
}

package() {
	cd "$srcdir/$_sourcedirectory/"
	DESTDIR="$pkgdir" dune install --prefix '/usr' --libdir '/usr/lib/ocaml' --docdir '/usr/share/doc' --mandir '/usr/share/man' --release --verbose

	for _folder in "$pkgdir/usr/share/doc/"*; do
		mv "$_folder" "$pkgdir/usr/share/doc/ocaml-$(basename "$_folder")"
	done

	install -dm755 "$pkgdir/usr/share/licenses/$pkgname"
	install -Dm644 'COPYING.txt' "$pkgdir/usr/share/licenses/$pkgname/COPYING.txt"
}
