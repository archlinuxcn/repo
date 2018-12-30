# Maintainer: Timothy Redaelli <timothy.redaelli@gmail.com>

pkgname="libnbcompat"
pkgver=20111103
pkgrel=1
pkgdesc="Portable NetBSD compatibility library"
arch=('i686' 'x86_64')
url="http://www.netbsd.org/"
license=('BSD')
makedepends=('bmake' 'cvs')

_cvsroot=":pserver:anoncvs@anoncvs.NetBSD.org:/cvsroot"
_cvsmod="pkgsrc/pkgtools/$pkgname/files"

build() {
  cd "$srcdir"
  msg "Connecting to NetBSD CVS server...."

  if [[ -d "$_cvsmod/CVS" ]]; then
    cd "$_cvsmod"
    cvs -z3 update -d
  else
    cvs -z3 -d "$_cvsroot" co -D "$pkgver" -f "$_cvsmod"
    cd "$_cvsmod"
  fi

  msg "CVS checkout done or server timeout"
  msg "Starting build..."

  rm -rf "$srcdir/$_cvsmod-build"
  cp -r "$srcdir/$_cvsmod" "$srcdir/$_cvsmod-build"
  cd "$srcdir/$_cvsmod-build"

  ./configure --prefix=/usr --enable-db --enable-bsd-getopt CPPFLAGS="${CPPFLAGS} -D_GNU_SOURCE"

  bmake
}

package() {
  cd "$srcdir/$_cvsmod-build"

  bmake install DESTDIR="$pkgdir/"
}
