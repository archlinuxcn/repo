# Maintainer: Daniel Peukert <dan.peukert@gmail.com>
# Contributor: Jakob Gahde <j5lx@fmail.co.uk>
_projectname='seq'
pkgname="ocaml-$_projectname"
pkgver='base'
_commit='cbb37092ecf7d4b3a5ff43a69aacbed19a4668e5'
pkgrel='4'
pkgdesc='Dummy backward-compatibility package for iterators'
arch=('x86_64' 'i686' 'arm' 'armv6h' 'armv7h' 'aarch64')
url="https://github.com/ocaml/opam-repository/tree/master/packages/$_projectname/$_projectname.$pkgver"
license=('custom:CC0')
depends=('ocaml>=4.07.0')
makedepends=('ocaml-findlib' 'opam')
options=('!strip')
source=(
	"$pkgname-$pkgver-$pkgrel-opam::https://raw.githubusercontent.com/ocaml/opam-repository/$_commit/packages/$_projectname/$_projectname.$pkgver/opam"
	"$pkgname-$pkgver-$pkgrel-META.seq::https://raw.githubusercontent.com/ocaml/opam-repository/$_commit/packages/$_projectname/$_projectname.$pkgver/files/META.seq"
	"$pkgname-$pkgver-$pkgrel-seq.install::https://raw.githubusercontent.com/ocaml/opam-repository/$_commit/packages/$_projectname/$_projectname.$pkgver/files/seq.install"
	"$pkgname-$pkgver-$pkgrel-COPYING::https://raw.githubusercontent.com/ocaml/opam-repository/$_commit/COPYING"
)
sha256sums=('4524608ea1de87fe2058d7eb39bd82cb001095bea65865254ec50fefad399d5c'
            'e95062b4d0519ef8335c02f7d0f1952d11b814c7ab7e6d566a206116162fa2be'
            'fff926c2c4d5a82b6c94c60c4c35eb06e3d39975893ebe6b1f0e6557cbe34904'
            '6d489af6292662d9e36d34ce49423784984a5f6e41d7b58f49b01264df59fa03')

_sourcedirectory="$_projectname-$pkgver"

prepare() {
	cd "$srcdir/"
	mkdir -p "$srcdir/$_sourcedirectory/files/"
	mv "$pkgname-$pkgver-$pkgrel-opam" "$srcdir/$_sourcedirectory/opam"
	mv "$pkgname-$pkgver-$pkgrel-COPYING" "$srcdir/$_sourcedirectory/COPYING"
	mv "$pkgname-$pkgver-$pkgrel-META.seq" "$srcdir/$_sourcedirectory/files/META.seq"
	mv "$pkgname-$pkgver-$pkgrel-seq.install" "$srcdir/$_sourcedirectory/files/seq.install"
}

package() {
	cd "$srcdir/$_sourcedirectory/files/"
	opam-installer --libdir="$pkgdir$(ocamlfind -printconf destdir)"
	install -Dm644 '../COPYING' "$pkgdir/usr/share/licenses/$pkgname/COPYING"
}
