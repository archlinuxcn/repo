# Maintainer: Daniel Peukert <daniel@peukert.cc>
# Contributor: Jakob Gahde <j5lx@fmail.co.uk>
_projectname='ppxlib'
pkgname="ocaml-$_projectname"
pkgver='0.27.0'
pkgrel='2'
pkgdesc='Standard library for ppx rewriters'
arch=('x86_64' 'i686' 'arm' 'armv6h' 'armv7h' 'aarch64')
url="https://github.com/ocaml-ppx/$_projectname"
license=('MIT')
depends=('ocaml>=4.04.1' 'ocaml-compiler-libs-repackaged>=0.11.0' 'ocaml-ppx_derivers>=1.0.0' 'ocaml-sexplib0>=0.12.0' 'ocaml-stdlib-shims')
makedepends=('dune>=2.7.0')
options=('!strip')
source=("$pkgname-$pkgver-$pkgrel.tar.gz::$url/archive/$pkgver.tar.gz")
sha512sums=('7d517e3896c25be116576a05e23cf3b862836b5dac8beabffe5fd475fca62aeb45b3e7be7483d3519c7b9ad618b6c7a0765d7d92e51da28e91c7dec784d6002e')

_sourcedirectory="$_projectname-$pkgver"

build() {
	cd "$srcdir/$_sourcedirectory/"
	dune build --release --verbose
}

# fails because of a circular dependency on this package by ppx_jane
# $pkgname-$pkgver-$pkgrel-fix-tests.diff::https://github.com/ocaml-ppx/ppxlib/pull/111
# check() {
#	cd "$srcdir/$_sourcedirectory/"
#	dune runtest --release --verbose
# }

package() {
	cd "$srcdir/$_sourcedirectory/"
	DESTDIR="$pkgdir" dune install --prefix '/usr' --libdir '/usr/lib/ocaml' --docdir '/usr/share/doc' --mandir '/usr/share/man' --release --verbose

	install -dm755 "$pkgdir/usr/share/licenses/$pkgname"
	ln -sf "/usr/share/doc/$pkgname/LICENSE.md" "$pkgdir/usr/share/licenses/$pkgname/LICENSE.md"
}
