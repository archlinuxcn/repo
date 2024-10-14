# Maintainer: oldherl <oldherl@gmail.com>
# Contributor: Anatoly V. Beregovoy <avberegovoy@gmail.com>

pkgname=libpasastro
pkgver=1.4.2
pkgrel=3
_pkgver="v$pkgver"
pkgdesc="Provide Pascal interface for standard astronomy libraries"
arch=('x86_64')
url="https://github.com/pchev/libpasastro"
license=('GPL-2.0-or-later')
depends=('gcc-libs')
makedepends=('git')
options=()
source=("git+https://github.com/pchev/libpasastro.git#tag=$_pkgver"
"https://github.com/pchev/libpasastro/pull/3.patch"
)
sha256sums=('98ebd671e59158a4218bca8976aa9d7520b2732e2dc5092f4a1d8f04d09543a4'
            '271ad2f7fd0ff4d8dfd6004cae563abfa5d2d1ba257947f8848215a30f8de0ef')

build() {
  cd $srcdir/$pkgname
  # fix: gcc complains if output directory does not exist
  mkdir -p plan404/obj
  # fix gcc14 issues
  patch -p1 -i ../3.patch
  make -j
}

package() {
  cd "$srcdir/$pkgname"
  make install PREFIX="$pkgdir/usr"
}

