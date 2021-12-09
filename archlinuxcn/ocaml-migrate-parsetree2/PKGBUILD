# Maintainer: Daniel Peukert <daniel@peukert.cc>
# Contributor: Jakob Gahde <j5lx@fmail.co.uk> (ocaml-migrate-parsetree PKGBUILD)
_projectname='ocaml-migrate-parsetree'
pkgname="${_projectname}2"
pkgver='2.3.0'
pkgrel='1'
pkgdesc='Convert OCaml parsetrees between different major versions - 2.x.x version'
arch=('x86_64' 'i686' 'arm' 'armv6h' 'armv7h' 'aarch64')
url="https://github.com/ocaml-ppx/$_projectname"
license=('custom:LGPL2.1 with linking exception')
depends=('ocaml>=4.02.3')
makedepends=('dune>=2.3.0')
options=('!strip')
source=(
	"$pkgname-$pkgver-$pkgrel.tar.gz::$url/archive/v$pkgver.tar.gz"
	"$pkgname.diff"
)
sha512sums=('f2000939eee0b2eac93d059292b0bc13aa809c9fe5e54b1e0bf412e41921647e9bc71ef23e0c6fba70e481891ece5a65763743932c69bf278a1036c437313219'
            '0809be6bb40f51cc034debf8083aa2a916aa36768af9e98a8a462e7136eb0e0b2ccced4afc90c1c1b46552689225b35e29b6f20dce549c655a0210da6bfebf63')

_sourcedirectory="$_projectname-$pkgver"

prepare() {
	cd "$srcdir/$_sourcedirectory/"
	patch --forward -p1 < "../$pkgname.diff"
}

build() {
	cd "$srcdir/$_sourcedirectory/"
	dune build --release --verbose
}

# fails because of a circular dependency on this package by lwt
# check() {
# 	cd "$srcdir/$_sourcedirectory/"
# 	dune runtest --release --verbose
# }

package() {
	cd "$srcdir/$_sourcedirectory/"
	DESTDIR="$pkgdir" dune install --prefix '/usr' --libdir 'lib/ocaml' --release --verbose

	install -dm755 "$pkgdir/usr/share/doc/$pkgname"
	mv "$pkgdir/usr/doc/$pkgname/"* "$pkgdir/usr/share/doc/$pkgname/"
	rm -r "$pkgdir/usr/doc/"

	install -dm755 "$pkgdir/usr/share/licenses/$pkgname"
	ln -sf "/usr/share/doc/$pkgname/LICENSE.md" "$pkgdir/usr/share/licenses/$pkgname/LICENSE.md"
}
