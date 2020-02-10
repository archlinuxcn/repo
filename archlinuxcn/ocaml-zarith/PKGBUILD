# Maintainer: Oliver Bandel <oliver@first.in-berlin.de>
# Submitter: Oliver Bandel <oliver@first.in-berlin.de>

pkgname=ocaml-zarith
provides=(zarith)
pkgver=1.8
pkgrel=2
pkgdesc='Implements arithmetic and logical operations over arbitrary-precision integers and rational numbers'
arch=(x86_64 i686)
url='https://github.com/ocaml/Zarith'
license=('GPL2')
depends=('gmp')
makedepends=('ocaml>=3.12.1' 'ocaml-findlib' )
source=("https://github.com/ocaml/Zarith/archive/release-${pkgver}.tar.gz")
md5sums=('c8757c1b1e7c30b990ccd830fb655c64')
sha256sums=('07e338621f9ab044ccf4fea784ff6c7ad92b03fc81c1c2b34d414675121bc6b2')

build() {
  cd Zarith-release-${pkgver}

  ./configure -installdir "${pkgdir}/usr/lib/ocaml" # install ignores DESTDIR
  make -j1
}

package() {
  cd Zarith-release-${pkgver}

  mkdir -p "${pkgdir}/usr/lib/ocaml"
  OCAMLFIND_LDCONF=ignore make install
}
