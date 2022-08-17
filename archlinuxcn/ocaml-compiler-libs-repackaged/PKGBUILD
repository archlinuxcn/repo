# Maintainer: Daniel Peukert <daniel@peukert.cc>
# Contributor: Felix Yan <felixonmars@archlinux.org>
# Contributor: Jakob Gahde <j5lx@fmail.co.uk>
_projectname='compiler-libs'
_pkgname="ocaml-$_projectname"
pkgname="$_pkgname-repackaged"
pkgver='0.12.4'
pkgrel='5'
pkgdesc='OCaml compiler libraries repackaged'
arch=('x86_64')
url="https://github.com/janestreet/$_pkgname"
license=('MIT')
depends=('ocaml>=4.04.1' 'ocaml-compiler-libs')
makedepends=('dune>=2.8.0')
options=('!strip')
source=("$pkgname-$pkgver-$pkgrel.tar.gz::$url/archive/v$pkgver.tar.gz")
sha512sums=('cf08e8d4bf25fff26a16a05036f08247176f4845d9d9ada85944c3fa89b6df9a5092d7a1025415a3b2ce00dd45b544cc82247648cf3952be2304e5d9ebab121d')

_sourcedirectory="$_pkgname-$pkgver"

build() {
	cd "$srcdir/$_sourcedirectory/"
	dune build --release --verbose
}

package() {
	cd "$srcdir/$_sourcedirectory/"
	DESTDIR="$pkgdir" dune install --prefix '/usr' --libdir '/usr/lib/ocaml' --docdir '/usr/share/doc' --mandir '/usr/share/man' --release --verbose

	install -dm755 "$pkgdir/usr/share/licenses/$pkgname"
	ln -sf "/usr/share/doc/$pkgname/LICENSE.md" "$pkgdir/usr/share/licenses/$pkgname/LICENSE.md"
}
