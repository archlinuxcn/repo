# Maintainer:  pandada8 <pandada8@gmail.com>
# Contributor: Harry Jeffery <harry|@|exec64|.|co|.|uk>
# Contributor: Alex Jordan <alexander3223098@gmail.com>
pkgname=zerotier-one-with-controller
pkgver=1.0.5
pkgrel=1
pkgdesc="Creates virtual Ethernet networks of almost unlimited size. controller node version"
arch=('i686' 'x86_64')
url="https://www.zerotier.com/index.html"
license=('GPL3')
groups=()
depends=("gcc-libs" "sqlite")
makedepends=()
conflicts=("zerotier-one" "zerotier-one-lastest")
source=("https://github.com/zerotier/ZeroTierOne/archive/$pkgver.tar.gz")
sha1sums=('de1dfb3ecc3bcbdea38388f51e91ac5927eba2b6')

build() {
  cd "$srcdir/ZeroTierOne-$pkgver"
  make ZT_ENABLE_NETWORK_CONTROLLER=1
}

check() {
  cd "$srcdir/ZeroTierOne-$pkgver"
  make ZT_ENABLE_NETWORK_CONTROLLER=1 selftest
}

package() {
  cd "$srcdir/ZeroTierOne-$pkgver"
  mkdir -p $pkgdir/var/lib/zerotier-one $pkgdir/usr/bin $pkgdir/usr/lib/systemd/system
  install zerotier-one $pkgdir/var/lib/zerotier-one
  install ext/installfiles/linux/systemd/zerotier-one.service $pkgdir/usr/lib/systemd/system
  cd $pkgdir/usr/bin
  ln -s ../../var/lib/zerotier-one/zerotier-one zerotier-cli
  ln -s ../../var/lib/zerotier-one/zerotier-one zerotier-idtool
}
