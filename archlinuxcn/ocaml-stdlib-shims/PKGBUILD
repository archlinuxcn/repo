# Maintainer: Daniel Peukert <dan.peukert@gmail.com>
_projectname='stdlib-shims'
pkgname="ocaml-$_projectname"
pkgver='0.2.0'
pkgrel='5'
pkgdesc='Shim to substitute `Pervasives` with `Stdlib` before 4.08'
arch=('x86_64' 'i686' 'arm' 'armv6h' 'armv7h' 'aarch64')
url="https://github.com/ocaml/$_projectname"
license=('custom:LGPL2.1 with linking exception')
depends=('ocaml>=4.02.3')
makedepends=('dune')
options=('!strip')
source=("$pkgname-$pkgver-$pkgrel.tar.gz::$url/archive/$pkgver.tar.gz")
sha256sums=('7151c71efd16d4e2a7dc1d4dcbcf6fdfbe2a07829428ffa6aac4b2586b1ce8c3')

_sourcedirectory="$_projectname-$pkgver"

build() {
	cd "$srcdir/$_sourcedirectory/"
	dune build -p "$_projectname" --verbose
}

check() {
	cd "$srcdir/$_sourcedirectory/"
	dune runtest -p "$_projectname" --verbose
}

package() {
	cd "$srcdir/$_sourcedirectory/"
	DESTDIR="$pkgdir" dune install --prefix '/usr' --libdir 'lib/ocaml'

	install -dm755 "$pkgdir/usr/share/doc/$pkgname"
	mv "$pkgdir/usr/doc/$_projectname/"* "$pkgdir/usr/share/doc/$pkgname/"
	rm -r "$pkgdir/usr/doc/"

	install -dm755 "$pkgdir/usr/share/licenses/$pkgname"
	ln -sf "/usr/share/doc/$pkgname/LICENSE" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
