# Contributor: Timo Schmiade <the_isz@gmx.de>
pkgname=gitstats-git
pkgver=264.0843039
pkgrel=1
pkgdesc="A statistics generator for git repositories."
arch=("any")
url="http://gitstats.sourceforge.net"
license=('GPL3')
groups=()
depends=('git' 'python2' 'gnuplot')
makedepends=('git')
source=("git://github.com/hoxu/gitstats.git#branch=master")
md5sums=("SKIP")

pkgver() {
  # In $startdir, we have a bare repo right after the sources have been fetched...
  cd "$startdir/gitstats"
  echo $(git rev-list --count master).$(git rev-parse --short master)
}

package() {
  # ... while in $srcdir, we get a "live" one.
  cd "$srcdir/gitstats"

  make install PREFIX="$pkgdir/usr" || return 1
  sed -i -e '1s/$/2/' "$pkgdir/usr/bin/gitstats"
} 

# vim:set ts=2 sw=2 et:
