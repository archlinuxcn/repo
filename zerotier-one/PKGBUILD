# Maintainer: Harry Jeffery <harry|@|exec64|.|co|.|uk>
# Contributor: Alex Jordan <alexander3223098@gmail.com>
pkgname=zerotier-one
pkgver=1.2.2
pkgrel=1
pkgdesc="Creates virtual Ethernet networks of almost unlimited size."
arch=('i686' 'x86_64' 'armv7h')
url="https://www.zerotier.com/index.html"
license=('GPL3')
groups=()
depends=("gcc-libs" "http-parser")
makedepends=("ruby-ronn")
source=("${pkgname}-${pkgver}::https://github.com/zerotier/ZeroTierOne/archive/$pkgver.tar.gz")
sha512sums=('ed510f91aa8b90a4b3e31c6da623adfe4a034bd15ad60b46a475834a91fb2a39d5d2c24d6910c1b7e2090d58c2ec6d103599c3e32519020942f5027866aa7ac4')

build() {
  cd "$srcdir/ZeroTierOne-$pkgver"
  make
}

check() {
  cd "$srcdir/ZeroTierOne-$pkgver"
  make selftest
  ./zerotier-selftest
}

package() {
  cd "$srcdir/ZeroTierOne-$pkgver"
  mkdir -p $pkgdir/var/lib/zerotier-one $pkgdir/usr/bin $pkgdir/usr/lib/systemd/system
  install zerotier-one $pkgdir/var/lib/zerotier-one
  install debian/zerotier-one.service $pkgdir/usr/lib/systemd/system
  chmod -x $pkgdir/usr/lib/systemd/system/zerotier-one.service
  cd $pkgdir/usr/bin
  ln -s /var/lib/zerotier-one/zerotier-one zerotier-cli
  ln -s /var/lib/zerotier-one/zerotier-one zerotier-idtool
  ln -s /var/lib/zerotier-one/zerotier-one zerotier-one
}
