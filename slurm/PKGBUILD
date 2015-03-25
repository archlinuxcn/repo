# Maintainer: Kyle Keen <keenerd@gmail.com>
# Contributor: Zhukov Pavel <gelios@gmail.com>
# Contributor: Christof Musik <christof@senfdax.de>
# Contributor: Falconindy
pkgname=slurm
pkgver=0.4.2
pkgrel=1
pkgdesc="Monitoring traffic statistics in realtime"
#url="http://www.wormulon.net/slurm"
#url="http://web.archive.org/web/20080304085911/http://www.wormulon.net/slurm"
url="https://github.com/mattthias/slurm/wiki"
license=("GPL")
arch=('i686' 'x86_64')
depends=('ncurses')
makedepends=('scons')
#source=(http://www.wormulon.net/files/code/slurm/$pkgname-$pkgver.tar.gz)
#source=(http://downloads.openwrt.org/sources/$pkgname-$pkgver.tar.gz)
source=(https://github.com/mattthias/$pkgname/archive/upstream/$pkgver.tar.gz)
md5sums=('b949aca331c25bf5c225faafc1948069')


build() {
  cd "$srcdir/$pkgname-upstream-$pkgver"
  #./configure --prefix=/usr CPPFLAGS=-D__Debian__
  #make
  scons
}

package() {
  cd "$srcdir/$pkgname-upstream-$pkgver"
  #make DESTDIR="$pkgdir" install
  install -Dm755 slurm "$pkgdir/usr/bin/slurm"

  # install themes
  install -dm755 "$pkgdir/usr/share/slurm"
  install -Dm644 -t "$pkgdir/usr/share/slurm" themes/*.theme 

  install -Dm644 slurm.1 "$pkgdir/usr/share/man/man1/slurm.1"
}
