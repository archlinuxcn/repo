# Maintainer: oldherl <oldherl@gmail.com>
# Contributor: Anatoly V. Beregovoy <avberegovoy@gmail.com>

pkgname=libpasastro
pkgver=1.4.3
pkgrel=1
_pkgver="v$pkgver"
pkgdesc="Provide Pascal interface for standard astronomy libraries"
arch=('x86_64')
url="https://github.com/pchev/libpasastro"
license=('GPL-2.0-or-later')
depends=('gcc-libs')
makedepends=('git')
options=()
source=("git+https://github.com/pchev/libpasastro.git#tag=$_pkgver"
)
sha256sums=('38f95945e0d63525a1f0dc7d0a7b66c3869f561ad58a28dea79be901d27ad5df')

build() {
  cd $srcdir/$pkgname
  # fix: gcc complains if output directory does not exist
  mkdir -p plan404/obj
  make -j
}

package() {
  cd "$srcdir/$pkgname"
  make install PREFIX="$pkgdir/usr"
}

