# Maintainer: Harry Jeffery <harry|@|exec64|.|co|.|uk>
# Contributor: Alex Jordan <alexander3223098@gmail.com>
pkgname=zerotier-one
pkgver=1.1.14
pkgrel=1
pkgdesc="Creates virtual Ethernet networks of almost unlimited size."
arch=('i686' 'x86_64' 'armv7h')
url="https://www.zerotier.com/index.html"
license=('GPL3')
groups=()
depends=("gcc-libs" "http-parser")
makedepends=("ruby-ronn")
source=("https://github.com/zerotier/ZeroTierOne/archive/$pkgver.tar.gz")
sha1sums=('b01a5167f8c9a28c80ed5fbae36c3b3cbbe55108')

build() {
  cd "$srcdir/ZeroTierOne-$pkgver"
  make
}

#check() {
#  cd "$srcdir/ZeroTierOne-$pkgver"
#  make selftest
#  ./zerotier-selftest
#}

package() {
  cd "$srcdir/ZeroTierOne-$pkgver"
  mkdir -p $pkgdir/var/lib/zerotier-one $pkgdir/usr/bin $pkgdir/usr/lib/systemd/system
  install zerotier-one $pkgdir/var/lib/zerotier-one
  install debian/zerotier-one.service $pkgdir/usr/lib/systemd/system
  chmod -x $pkgdir/usr/lib/systemd/system/zerotier-one.service
  cd $pkgdir/usr/bin
  ln -s ../../var/lib/zerotier-one/zerotier-one zerotier-cli
  ln -s ../../var/lib/zerotier-one/zerotier-one zerotier-idtool
  ln -s ../../var/lib/zerotier-one/zerotier-one zerotier-one
}
