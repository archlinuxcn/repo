# Maintainer: Harry Jeffery <harry|@|exec64|.|co|.|uk>
# Contributor: Alex Jordan <alexander3223098@gmail.com>
pkgname=zerotier-one
pkgver=1.2.4
pkgrel=1
pkgdesc="Creates virtual Ethernet networks of almost unlimited size."
arch=('i686' 'x86_64' 'armv7h')
url="https://www.zerotier.com/index.html"
license=('GPL3')
groups=()
depends=("gcc-libs" "http-parser")
makedepends=("ruby-ronn")
source=("${pkgname}-${pkgver}::https://github.com/zerotier/ZeroTierOne/archive/$pkgver.tar.gz")
sha512sums=('82adb110208d24ae2745e3839810afcac87955de050ebfe0517a7dc2a875881dafd40c1b16a041742d8c4d0f6513abcc71d6ea3e06c2fb89b47be2630a500363')

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
