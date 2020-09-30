# Maintainer: Daniel Peukert <dan.peukert@gmail.com>
# Contributor: Jakob Gahde <j5lx@fmail.co.uk>
_projectname='compiler-libs'
_pkgname="ocaml-$_projectname"
pkgname="$_pkgname-repackaged"
pkgver='0.12.3'
pkgrel='1'
pkgdesc='OCaml compiler libraries repackaged'
arch=('x86_64' 'i686' 'arm' 'armv6h' 'armv7h' 'aarch64')
url="https://github.com/janestreet/$_pkgname"
license=('MIT')
depends=('ocaml>=4.04.1')
makedepends=('dune>=1.5.1')
options=('!strip')
source=("$pkgname-$pkgver-$pkgrel.tar.gz::$url/archive/v$pkgver.tar.gz")
sha256sums=('86b23bf8df2e027ecfc04f6a326cdc87f27b2e3790860fbc28aabb9d0c2cc174')

_sourcedirectory="$_pkgname-$pkgver"

build() {
	cd "$srcdir/$_sourcedirectory/"
	dune build -p "$_pkgname" --verbose
}

package() {
	cd "$srcdir/$_sourcedirectory/"
	DESTDIR="$pkgdir" dune install --prefix '/usr' --libdir 'lib/ocaml'

	install -dm755 "$pkgdir/usr/share/doc/$pkgname"
	mv "$pkgdir/usr/doc/$_pkgname/"* "$pkgdir/usr/share/doc/$pkgname/"
	rm -r "$pkgdir/usr/doc/"

	install -dm755 "$pkgdir/usr/share/licenses/$pkgname"
	ln -sf "/usr/share/doc/$pkgname/LICENSE.md" "$pkgdir/usr/share/licenses/$pkgname/LICENSE.md"
}
