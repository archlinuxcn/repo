# Maintainer: Moritz Lipp <mlq@pwmt.org>
pkgname=libunwind-git
pkgver=2c3444d
pkgrel=1
pkgdesc="Portable and efficient C programming interface (API) to determine the call-chain of a program"
arch=('i686' 'x86_64')
url="http://www.nongnu.org/libunwind/"
license=('GPL')
makedepends=('git' 'texlive-core')
depends=('glibc')
provides=('libunwind')
conflicts=('libunwind')

source=("${pkgname}::git+git://git.sv.gnu.org/libunwind.git")
sha1sums=('SKIP')

build() {
  cd "$srcdir/$pkgname"

  autoreconf -i
  ./configure CFLAGS="$CFLAGS -U_FORTIFY_SOURCE" --prefix=/usr
  make
}

check() {
  cd "$srcdir/$pkgname"
  PATH=/usr/bin:$PATH make check || return 0
}

package() {
  cd "$srcdir/$pkgname"
  make DESTDIR="$pkgdir/" install
}

pkgver() {
  cd "$srcdir/$pkgname"
  local ver="$(git describe --long --always)"
  printf "%s" "${ver//-/.}"
}

# vim:set ts=2 sw=2 et:
