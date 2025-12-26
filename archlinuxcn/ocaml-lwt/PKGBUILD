# Maintainer: Manuel Wiesinger <m {you know what belongs here} mmap {and here} at>
# Contributor: Daniel Peukert <daniel@peukert.cc>
# Contributor: Jakob Gahde <j5lx@fmail.co.uk>
# Contributor: Serge Zirukin <ftrvxmtrx@gmail.com>
# Contributor: Sergei Lebedev <superbobry@gmail.com
# Contributor: serp <serp256 at gmail dot com>
_projectname='lwt'
pkgname="ocaml-$_projectname"
pkgver='5.9.2'
pkgrel='1'
pkgdesc='A library for cooperative threads in OCaml'
arch=('x86_64' 'aarch64')
url="https://github.com/ocsigen/$_projectname"
license=('MIT')
depends=(
    'dune>=3.15.0'
    'libev'
    'ocaml-findlib>=1.7.3'
    'ocaml-ocplib-endian'
    'ocaml-ppxlib>=0.36.0'
    'ocaml-react>=1.0.0'
    'ocaml>=5.1.0'
    'zstd'
)
makedepends=('cppo>=1.1.0')
checkdepends=('ocaml-ppx_let>=0.17.1')
options=('!strip')
source=("$pkgname-$pkgver.tar.gz::$url/archive/$pkgver.tar.gz")
b2sums=('8256236014992e4a009b34944e01215502c5f25a9979cafdbb2c93b4e4aa0c20717cf8a101ed43fec7f61d8213c73fd572058f87f800a6e034c681074fe93f56')

_sourcedirectory="$_projectname-$pkgver"

prepare() {
	cd "$srcdir/$_sourcedirectory/"

	# This test breaks for some people but not for others, see comments from oriba, crave and pha-qu on the AUR page
	sed -i '/test_mcast "mcast-join-loop"/d' 'test/unix/test_mcast.ml'
}

build() {
	cd "$srcdir/$_sourcedirectory/"
	LWT_DISCOVER_ARGUMENTS='--use-libev true --use-pthread true --libev-default true --verbose' dune build --release --verbose
}

check() {
	cd "$srcdir/$_sourcedirectory/"
	dune runtest --release --verbose
}

package() {
	cd "$srcdir/$_sourcedirectory/"
	DESTDIR="$pkgdir" dune install --prefix '/usr' --libdir '/usr/lib/ocaml' --docdir '/usr/share/doc/ocaml' --mandir '/usr/share/man' --release --verbose

	install -dm755 "$pkgdir/usr/share/licenses/$pkgname"
	ln -sf "/usr/share/doc/ocaml/$_projectname/LICENSE.md" "$pkgdir/usr/share/licenses/$pkgname/MIT"
}
