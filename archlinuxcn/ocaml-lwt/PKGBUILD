# Maintainer: Manuel Wiesinger <m {you know what belongs here} mmap {and here} at>
# Contributor: Daniel Peukert <daniel@peukert.cc>
# Contributor: Jakob Gahde <j5lx@fmail.co.uk>
# Contributor: Serge Zirukin <ftrvxmtrx@gmail.com>
# Contributor: Sergei Lebedev <superbobry@gmail.com
# Contributor: serp <serp256 at gmail dot com>

_ocamlname='lwt'
pkgname="ocaml-$_ocamlname"
pkgver='6.1.0'
pkgrel='1'
pkgdesc='A library for cooperative threads in OCaml'
arch=('x86_64' 'aarch64')
url="https://github.com/ocsigen/$_ocamlname"
license=('MIT')
depends=(
	'dune>=3.18.0'
	'glibc'
	'libev'
	'ocaml-ocplib-endian'
	'ocaml-ppxlib>=0.36.0'
	'ocaml-react>=1.0.0'
	'ocaml>=4.14'
	'zstd'
)
makedepends=(
	'cppo>=1.1.0'
	'ocaml-findlib>=1.7.3'
)
options=('!strip')
source=("$pkgname-$pkgver.tar.gz::$url/archive/$pkgver.tar.gz")
b2sums=('b46a6a6d23e81b4d96b9e6a7944ebd1b492674cfc7f63a79e8b0776550dea7df922e26288d659ecc781d7d81fd27e931f74090793f43e9fa7faa511427bd32d0')

prepare()
{
	cd $_ocamlname-$pkgver

	# This test breaks for some people but not for others, see comments from
	# oriba, crave and pha-qu on the AUR page
	sed -i '/test_mcast "mcast-join-loop"/d' 'test/unix/test_mcast.ml'
}

build()
{
	cd $_ocamlname-$pkgver

	LWT_DISCOVER_ARGUMENTS='--use-libev true --use-pthread true --libev-default true --verbose' \
						  dune \build \
						  --release \
						  --verbose
}

check()
{
	cd $_ocamlname-$pkgver

	dune runtest \
		 --release \
		 --verbose
}

package()
{
	cd $_ocamlname-$pkgver

	DESTDIR="$pkgdir" \
		   dune install \
		   --prefix '/usr' \
		   --libdir '/usr/lib/ocaml' \
		   --docdir '/usr/share/doc/ocaml' \
		   --mandir '/usr/share/man' \
		   --release \
		   --verbose

	install -dm755 $pkgdir/usr/share/licenses/$pkgname
	ln -sf /usr/share/doc/ocaml/$_ocamlname/LICENSE.md $pkgdir/usr/share/licenses/$pkgname/MIT
}
