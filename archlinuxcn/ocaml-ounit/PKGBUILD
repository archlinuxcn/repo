# Maintainer: Daniel Peukert <dan.peukert@gmail.com>
# Contributor: Eric Bailey <nerflad@gmail.com>
# Contributor: Marek Kubica <marek@xivilization.net>
# Contributor: Serge Zirukin <ftrvxmtrx@gmail.com>
# Contributor: Sergei Lebedev <superbobry@gmail.com>
# Contributor: Thomas S Hatch <thatch45 at gmail dot com>
# Contributor: Sebastian Wiesner <lunaryorn googlemail com>
# Contributor: Benjamin Andresen <benny(at)klapmuetz(dot)org>
# Contributor: Sylvester Johansson <syljo361(at)gmail(dot)org>
_projectname='ounit'
pkgname="ocaml-$_projectname"
pkgver='2.2.2'
pkgrel='2'
pkgdesc='Unit testing framework for OCaml'
arch=('x86_64' 'i686' 'arm' 'armv6h' 'armv7h' 'aarch64')
url="https://github.com/gildor478/$_projectname"
license=('MIT')
depends=('ocaml' 'ocaml-lwt' 'ocaml-stdlib-shims')
makedepends=('dune' 'ocaml-findlib')
options=('!strip')
source=("$pkgname-$pkgver-$pkgrel.tar.gz::$url/archive/v$pkgver.tar.gz")
sha256sums=('db5dbdd4fd29a9ff82dd9d75813e0391d833ba868f813e3c3349807bc9da5032')

_sourcedirectory="$_projectname-$pkgver"

build() {
	cd "$srcdir/$_sourcedirectory/"
	dune build -p "${_projectname},${_projectname}-lwt,${_projectname}2,${_projectname}2-lwt" --verbose
}

check() {
	cd "$srcdir/$_sourcedirectory/"
	dune runtest -p "${_projectname},${_projectname}-lwt,${_projectname}2,${_projectname}2-lwt" --verbose
}

package() {
	cd "$srcdir/$_sourcedirectory/"
	DESTDIR="$pkgdir" dune install --prefix '/usr' --libdir 'lib/ocaml'

	install -dm755 "$pkgdir/usr/share/doc/$pkgname"
	mv "$pkgdir/usr/doc/$_projectname/"* "$pkgdir/usr/share/doc/$pkgname/"
	rm -r "$pkgdir/usr/doc/"

	install -dm755 "$pkgdir/usr/share/licenses/$pkgname"
	ln -sf "/usr/share/doc/$pkgname/LICENSE.txt" "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
