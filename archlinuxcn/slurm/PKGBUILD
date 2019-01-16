# Maintainer: Kyle Keen <keenerd@gmail.com>
# Contributor: Zhukov Pavel <gelios@gmail.com>
# Contributor: Christof Musik <christof@senfdax.de>
# Contributor: Falconindy
pkgname=slurm
pkgver=0.4.3
pkgrel=1
pkgdesc="Monitoring traffic statistics in realtime"
#url="http://www.wormulon.net/slurm"
#url="http://web.archive.org/web/20080304085911/http://www.wormulon.net/slurm"
url="https://github.com/mattthias/slurm/wiki"
license=("GPL")
arch=('i686' 'x86_64')
depends=('ncurses')
makedepends=('cmake')
#source=(http://www.wormulon.net/files/code/slurm/$pkgname-$pkgver.tar.gz)
#source=(http://downloads.openwrt.org/sources/$pkgname-$pkgver.tar.gz)
source=(https://github.com/mattthias/$pkgname/archive/upstream/$pkgver.tar.gz)
md5sums=('ff39b8e1fd31274ba1bb36d4aadc1d48')


build() {
  cd "$srcdir/$pkgname-upstream-$pkgver"
  #./configure --prefix=/usr CPPFLAGS=-D__Debian__
  #scons
  mkdir -p build
  cd build
  cmake -DCMAKE_INSTALL_PREFIX=/usr ..
  make
}

package() {
  cd "$srcdir/$pkgname-upstream-$pkgver/build"
  make DESTDIR="$pkgdir" install
  install -Dm644 ../slurm.1 "$pkgdir/usr/share/man/man1/slurm.1"
}
