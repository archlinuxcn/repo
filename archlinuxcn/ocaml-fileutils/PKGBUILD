# Maintainer: Thorsten Wißmann <edu@thorsten-wissmann.de>
# Contributor: Serge Zirukin <ftrvxmtrx@gmail.com>
# Contributor: Sergei Lebedev <superbobry@gmail.com>
# Contributor: Magnus Therning <magnus@therning.org>
# Contributor: Thomas Pani <thomas.pani@gmail.com>
# Contributor: crave <crave@infinity>

pkgname=ocaml-fileutils
pkgver=0.5.3
oldver=0.4.5
pkgrel=1
pkgdesc="A library to provide pure OCaml functions to manipulate real file and filename."
arch=('i686' 'x86_64')
url="http://forge.ocamlcore.org/projects/ocaml-fileutils"
license=('LGPL')
depends=('ocaml')
makedepends=('ocaml-findlib' 'ocaml-ounit' 'ocamlbuild')
source=('https://forge.ocamlcore.org/frs/download.php/1728/ocaml-fileutils-0.5.3.tar.gz')
md5sums=('9b719b19b96525004c88bf7bc846fa1d')

build() {
  cd "$srcdir/"*/
  ocaml setup.ml -configure --prefix prefix
  ocaml setup.ml -build
}

package() {
  cd "$srcdir/"*/
  export OCAMLFIND_DESTDIR="$pkgdir$(ocamlfind printconf destdir)"
  install -dm 755 "$OCAMLFIND_DESTDIR"
  ocaml setup.ml -install
  install -Dm 644 COPYING.txt "$pkgdir/usr/share/licenses/$pkgname/COPYING"
}
