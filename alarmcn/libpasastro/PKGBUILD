# Maintainer: oldherl <oldherl@gmail.com>
# Contributor: Anatoly V. Beregovoy <avberegovoy@gmail.com>

pkgname=libpasastro
pkgver=1.4.4
pkgrel=1
_pkgver="v$pkgver"
pkgdesc="Provide Pascal interface for standard astronomy libraries"
arch=('x86_64' 'aarch64')
url="https://github.com/pchev/libpasastro"
license=('GPL-2.0-or-later')
depends=('gcc-libs')
makedepends=('git')
options=()
source=("git+https://github.com/pchev/libpasastro.git#tag=$_pkgver"
)
sha256sums=('c75f91d93ef4a308a4dbfe995a8a79f335d8b7708f7cf3f2cb559f928e769ea7')

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

